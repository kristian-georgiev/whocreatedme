import os
import inspect


def create_dotfile(script_path, name_of_file_being_saved) -> None:
    """Create a dotfile with the path to the script that created the given file & the source code of the script."""
    fn = os.path.basename(name_of_file_being_saved)
    dotfile_name = f".{fn}.who"

    separator = "\n" + "-" * 80 + "\n"
    # Read the source code of the current script
    with open(script_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    with open(dotfile_name, "w", encoding="utf-8") as dotfile:
        dotfile.write(f"Script Path: {script_path}\n")
        dotfile.write(separator)
        dotfile.write("Code:\n")
        dotfile.write(source_code)


def patch_numpy_save(script_path) -> None:
    """Patch numpy.save to automatically create a dotfile."""
    import numpy as np  # noqa: F402

    _original_save_np = np.save

    def _new_save_np(file, arr, allow_pickle=True, fix_imports=True):
        """A wrapper around the original numpy.save function."""
        _original_save_np(file, arr, allow_pickle=allow_pickle, fix_imports=fix_imports)
        create_dotfile(script_path, file)

    np.save = _new_save_np
    print("numpy.save is patched and will create a dotfile for each file saved")


def patch_torch_save(script_path) -> None:
    """Patch torch.save to automatically create a dotfile."""
    import torch  # noqa: F402
    import pickle  # noqa: F402

    _original_save_ch = torch.save

    def _new_save_pt(
        obj, f, pickle_module=pickle, pickle_protocol=pickle.HIGHEST_PROTOCOL
    ):
        """A wrapper around the original torch.save function."""
        _original_save_ch(
            obj, f, pickle_module=pickle_module, pickle_protocol=pickle_protocol
        )
        create_dotfile(script_path, f)

    torch.save = _new_save_pt
    print("torch.save is patched and will create a dotfile for each file saved")


def get_script_path() -> str:
    """Get the path to the script that called this function."""
    stack = inspect.stack()
    try:
        caller_frame = stack[2]
        caller_module = inspect.getmodule(caller_frame[0])
        _script_path = os.path.abspath(caller_module.__file__)
    except (IndexError, AttributeError):
        _script_path = "Unknown"
    return _script_path


def trace(numpy=False, torch=False) -> None:
    """Patch numpy.save and/or torch.save to automatically create a dotfile."""
    script_path = get_script_path()
    if numpy:
        patch_numpy_save(script_path)
    if torch:
        patch_torch_save(script_path)
