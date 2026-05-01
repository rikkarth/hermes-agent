from prompt_toolkit.input.ansi_escape_sequences import ANSI_SEQUENCES
from prompt_toolkit.keys import Keys

from cli import _SHIFT_ENTER_KEY, _SHIFT_SPACE_KEY


def test_shift_space_sequences_are_registered():
    assert ANSI_SEQUENCES["\x1b[32;2u"] == _SHIFT_SPACE_KEY
    assert ANSI_SEQUENCES["\x1b[27;2;32~"] == _SHIFT_SPACE_KEY


def test_shift_enter_sequences_are_registered():
    assert ANSI_SEQUENCES["\x1b[13;2u"] == _SHIFT_ENTER_KEY
    assert ANSI_SEQUENCES["\x1b[27;2;13~"] == _SHIFT_ENTER_KEY


def test_modified_backspace_sequences_are_registered():
    assert ANSI_SEQUENCES["\x1b[127;2u"] == Keys.ControlH
    assert ANSI_SEQUENCES["\x1b[27;2;127~"] == Keys.ControlH
