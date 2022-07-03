import pytest
from hash_practice.exercises import *

def test_will_return_empty_list_for_an_empty_list():
    # Arrange
    words = []

    # Act-Assert
    assert grouped_anagrams(words) == []

def test_will_return_correct_result_for_readme_example():
    # Arrange
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    # Act
    answer = grouped_anagrams(words)
    expected_answer = [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
        ]

    # Assert
    assert len(answer) == 3
    for words in answer:
        words.sort()
        assert words in expected_answer

def test_will_work_for_strings_that_are_all_anagrams():
    # Arrange
    words = ["eat", "tae", "tea", "eta", "aet", "ate"]
    expected_answer = [["eat", "tae", "tea", "eta", "aet", "ate"]]

    # Act
    answer = grouped_anagrams(words)

    # Assert
    assert answer == expected_answer


def test_will_work_for_strings_which_are_all_not_anagrams():
    # Arrange
    words = ["eat", "ear", "tar", "pop", "pan", "pap"]

    # Act
    answer = grouped_anagrams(words)
    expected_answer = [
        ["eat"],
        ["ear"],
        ["tar"],
        ["pop"],
        ["pan"],
        ["pap"]
      ];

    # Assert
    assert len(answer) == 6

    for anagrams in expected_answer:
        assert len(anagrams) == 1
        assert anagrams in expected_answer


def test_will_work_for_strings_which_are_longer_words():
    # Arrange
    words = ["bored", "players", "sadder", "dreads", "robed", "parsley"]

    # Act
    answer = grouped_anagrams(words)
    expected_answer = [
        ["bored", "robed"],
        ["parsley", "players"],
        ["dreads", "sadder"],
    ];

    # Assert
    assert len(answer) == 3

    for anagrams in answer:
        anagrams.sort()
        assert anagrams in expected_answer
