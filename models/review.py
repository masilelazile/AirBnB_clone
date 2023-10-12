#!/usr/bin/python3
"""Defines the Review class."""
from model.base_modesl import BaseModel


class Review(BaseModel):
    """Represents a review.
    Attributes:
    place_id (str): The Place id.
    user_id (str): The User id.
    text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
