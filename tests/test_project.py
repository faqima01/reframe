#!/usr/bin/env python3
# encoding: UTF-8
"""
Test of Reframe's Project operator
@contributor: Massi Faqiri
@date: 10/14/2019
"""
import pytest
from reframe import Relation
import pandas as pd
import csv

country = Relation("country.csv")


@pytest.fixture
def project_data_from_csv():
    """Returns a list of lists each of which contains the list of continents, regions and government forms, extracted from the country.csv file."""
    continents = []
    regions = []
    gov_forms = []

    with open("country.csv", encoding="utf8") as country_csv:
        csv_reader = csv.reader(country_csv, delimiter="|")
        for row in csv_reader:
            cont = row[2]
            reg = row[3]
            gov = row[11]
            if cont not in continents and cont != "continent":
                continents.append(cont)
            if reg not in regions and reg != "region":
                regions.append(reg)
            if gov not in gov_forms and gov != "governmentform":
                gov_forms.append(gov)

    data_list = [continents, regions, gov_forms]
    return data_list


def test_project_continent(project_data_from_csv):
    """Asserts the equality of the dataframe of continents created through Project operator using reframe library and the dataframe created from the list extracted from the csv file."""
    continents_data = {"continent": project_data_from_csv[0]}
    df = pd.DataFrame(continents_data)
    assert (
        country.project(["continent"])
        .reset_index(drop=True)
        .equals(df.reset_index(drop=True))
    )


def test_project_region(project_data_from_csv):
    """Asserts the equality of the dataframe of continents created through Project operator using reframe library and the dataframe created from the list extracted from the csv file."""
    region_data = {"region": project_data_from_csv[1]}
    df = pd.DataFrame(region_data)
    assert (
        country.project(["region"])
        .reset_index(drop=True)
        .equals(df.reset_index(drop=True))
    )


def test_project_govforms(project_data_from_csv):
    """Asserts the equality of the dataframe of government forms created through Project operator using reframe library and the dataframe created from the list extracted from the csv file."""
    govforms_data = {"governmentform": project_data_from_csv[2]}
    df = pd.DataFrame(govforms_data)
    assert (
        country.project(["governmentform"])
        .reset_index(drop=True)
        .equals(df.reset_index(drop=True))
    )