import argparse
import ctypes
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path, PurePosixPath


MOD_ID = "votc_community_edition"
MOD_FILE_NAME = f"{MOD_ID}.mod"
SOURCE_DESCRIPTOR_NAME = "descriptor.mod"
INCLUDED_FOLDERS = ("common", "events", "gfx", "gui", "localization")
INCLUDED_FILES = ("README.md",)


def archive_path(*parts):
    return str(PurePosixPath(*parts))


def is_relative_to(path, parent):
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def find_documents_dir():
    """尽量获取当前用户真正的“文档”目录，兼容 OneDrive/重定向文档。"""
    if os.name == "nt":
        try:
            class GUID(ctypes.Structure):
                _fields_ = (
                    ("Data1", ctypes.c_uint32),
                    ("Data2", ctypes.c_uint16),
                    ("Data3", ctypes.c_uint16),
                    ("Data4", ctypes.c_ubyte * 8),
                )

            folder_id_documents = GUID(
                0xFDD39AD0,
                0x238F,
                0x46AF,
                (ctypes.c_ubyte * 8)(0xAD, 0xB4, 0x6C, 0x85, 0x48, 0x03, 0x69, 0xC7),
            )
            path_ptr = ctypes.c_wchar_p()
            ctypes.windll.shell32.SHGetKnownFolderPath.argtypes = (
                ctypes.POINTER(GUID),
                ctypes.c_uint32,
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_wchar_p),
            )
            ctypes.windll.shell32.SHGetKnownFolderPath.restype = ctypes.c_long
            ctypes.windll.ole32.CoTaskMemFree.argtypes = (ctypes.c_void_p,)
            ctypes.windll.ole32.CoTaskMemFree.restype = None
            result = ctypes.windll.shell32.SHGetKnownFolderPath(
                ctypes.byref(folder_id_documents), 0, None, ctypes.byref(path_ptr)
            )
            if result == 0 and path_ptr.value:
                documents = Path(path_ptr.value)
                ctypes.windll.ole32.CoTaskMemFree(ctypes.cast(path_ptr, ctypes.c_void_p))
                return documents
        except Exception:
            pass

    user_profile = os.environ.get("USERPROFILE")
    if user_profile:
        return Path(user_profile) / "Documents"
    return Path.home() / "Documents"


def default_ck3_user_dir():
    return find_documents_dir() / "Paradox Interactive" / "Crusader Kings III"


def default_mod_dir():
    return default_ck3_user_dir() / "mod"


def source_mod_dir():
    return Path(__file__).resolve().parent


def get_version_from_mod_file(mod_file_path):
    """从 mod 文件中提取版本号。"""
    try:
        content = mod_file_path.read_text(encoding="utf-8")
        version_match = re.search(r'version="([^"]+)"', content)
        if version_match:
            return version_match.group(1)
        raise ValueError("无法在 mod 文件中找到版本号")
    except Exception as e:
        print(f"读取 mod 文件时出错: {e}")
        return None


def descriptor_text(source_descriptor, target_folder_name=MOD_ID, include_path=True, strip_remote_id=False):
    content = source_descriptor.read_text(encoding="utf-8").strip()
    content = re.sub(r'(?m)^path="[^"]*"\s*$', "", content).strip()
    if strip_remote_id:
        # 本地安装副本不应携带创意工坊 ID，避免与已订阅的 Workshop 版本冲突。
        content = re.sub(r'(?m)^remote_file_id="[^"]*"\s*$', "", content).strip()
    if include_path:
        content = f'{content}\npath="mod/{target_folder_name}"'
    return f"{content}\n"


def copy_mod_files(source_dir, target_dir, clean=True):
    if clean and target_dir.exists():
        source_resolved = source_dir.resolve()
        target_resolved = target_dir.resolve()
        if source_resolved == target_resolved or is_relative_to(source_resolved, target_resolved):
            raise ValueError(f"目标目录不能是源码目录或源码目录的上级: {target_dir}")
        shutil.rmtree(target_dir)

    target_dir.mkdir(parents=True, exist_ok=True)

    for folder in INCLUDED_FOLDERS:
        source = source_dir / folder
        target = target_dir / folder
        if source.exists():
            print(f"复制文件夹: {folder}")
            shutil.copytree(source, target, dirs_exist_ok=True)
        else:
            print(f"警告: 文件夹 {folder} 不存在")

    for file_name in INCLUDED_FILES:
        source = source_dir / file_name
        target = target_dir / file_name
        if source.exists():
            print(f"复制文件: {file_name}")
            shutil.copy2(source, target)
        else:
            print(f"警告: 文件 {file_name} 不存在")


def install_mod(mod_dir=None, clean=True):
    source_dir = source_mod_dir()
    source_descriptor = source_dir / SOURCE_DESCRIPTOR_NAME
    if not source_descriptor.exists():
        print(f"找不到 mod 描述文件: {source_descriptor}")
        return 1

    mod_dir = Path(mod_dir).expanduser().resolve() if mod_dir else default_mod_dir()
    target_dir = mod_dir / MOD_ID
    root_descriptor = mod_dir / MOD_FILE_NAME

    print(f"源目录: {source_dir}")
    print(f"安装目录: {target_dir}")

    mod_dir.mkdir(parents=True, exist_ok=True)
    copy_mod_files(source_dir, target_dir, clean=clean)

    root_descriptor.write_text(
        descriptor_text(source_descriptor, include_path=True, strip_remote_id=True),
        encoding="utf-8",
    )
    (target_dir / "descriptor.mod").write_text(
        descriptor_text(source_descriptor, include_path=False),
        encoding="utf-8",
    )

    print(f"已写入启动器描述文件: {root_descriptor}")
    print("安装完成。请在 CK3 启动器中启用 Voices of the Court 2.0 - Community Edition（本地版）。")
    return 0


def create_mod_package(output_dir=None):
    source_dir = source_mod_dir()
    mod_file_path = source_dir / SOURCE_DESCRIPTOR_NAME

    version = get_version_from_mod_file(mod_file_path)
    if not version:
        print("无法获取版本号，终止打包")
        return 1

    output_dir = Path(output_dir).expanduser().resolve() if output_dir else source_dir.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_name = f"{MOD_ID}{version}.zip"
    zip_path = output_dir / zip_name

    print(f"正在创建压缩包: {zip_name}")
    print(f"版本号: {version}")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for folder in INCLUDED_FOLDERS:
            folder_path = source_dir / folder
            if folder_path.exists():
                print(f"添加文件夹: {folder}")
                for file_path in folder_path.rglob("*"):
                    if file_path.is_file():
                        arcname = archive_path(
                            MOD_ID,
                            folder,
                            file_path.relative_to(folder_path).as_posix(),
                        )
                        zipf.write(file_path, arcname)
            else:
                print(f"警告: 文件夹 {folder} 不存在")

        for file_name in INCLUDED_FILES:
            file_path = source_dir / file_name
            if file_path.exists():
                print(f"添加文件到 {MOD_ID} 文件夹内: {file_name}")
                zipf.write(file_path, archive_path(MOD_ID, file_name))
            else:
                print(f"警告: 文件 {file_name} 不存在")

        zipf.writestr(
            MOD_FILE_NAME,
            descriptor_text(mod_file_path, include_path=True),
        )
        zipf.writestr(
            archive_path(MOD_ID, "descriptor.mod"),
            descriptor_text(mod_file_path, include_path=False),
        )

    print(f"压缩包创建完成: {zip_path}")
    return 0


def parse_args():
    parser = argparse.ArgumentParser(
        description="安装或打包 Voices of the Court 2.0 Community Edition (2CE) 的 CK3 mod 文件。"
    )
    subparsers = parser.add_subparsers(dest="command")

    install_parser = subparsers.add_parser(
        "install",
        help="安装到当前用户文档中的 CK3 mod 目录",
    )
    install_parser.add_argument(
        "--mod-dir",
        help="自定义 CK3 mod 目录；默认使用当前用户文档下的 Paradox Interactive/Crusader Kings III/mod",
    )
    install_parser.add_argument(
        "--no-clean",
        action="store_true",
        help="不清空目标 mod 文件夹，直接覆盖复制文件",
    )

    package_parser = subparsers.add_parser("package", help="创建发布用 zip 包")
    package_parser.add_argument(
        "--output-dir",
        help="zip 输出目录；默认输出到 voices_of_the_court_mod2 ce 的上级目录",
    )

    parser.set_defaults(command="install", mod_dir=None, no_clean=False)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.command == "package":
        sys.exit(create_mod_package(args.output_dir))
    sys.exit(install_mod(args.mod_dir, clean=not args.no_clean))
