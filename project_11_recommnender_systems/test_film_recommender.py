import pytest
from film_recommender import get_recommendations


def test_output_length():
    """Test if the output of get_recommendations has the right length"""
    output = get_recommendations("Titanic", "5")
    assert len(output) == 3


def test_datatypes():
    """Test that get_recommendations returns the right datatype"""
    output = get_recommendations("Titanic", "2")
    for movie in output:
        assert isinstance(movie, str)


def test_too_many_input_parameters():
    """Test that get_recommendations does not work if the the user passes to many input parameters"""
    with pytest.raises(TypeError):
        output = get_recommendations("Titanic", "2", 2)
