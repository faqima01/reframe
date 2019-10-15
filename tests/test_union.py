#!/usr/bin/env python3
# encoding: UTF-8
"""
Test of Reframe's Union operator
@contributor: Massi Faqiri
@date: 10/14/2019
"""
import pytest
from reframe import Relation
import pandas as pd
import csv

country = Relation("country.csv")

@pytest.fixture
def unions_masterdata():
    """Returns the masterlist of lists each of which contains the result of the union of country data by two specific regions, two specific government forms and two specific continents."""
    reg1_name_list = []
    reg1_region_list = []
    reg2_name_list = []
    reg2_region_list = []
    gov1_name_list = []
    gov1_govform_list = []
    gov2_name_list = []
    gov2_govform_list = []
    cont1_name_list = []
    cont1_cont_list = []
    cont2_name_list = []
    cont2_cont_list = []

    with open("country.csv", encoding="utf8") as country_csv:
        csv_reader = csv.reader(country_csv, delimiter="|")
        for row in csv_reader:
            if row[3] == "North America":
                reg1_name_list.append(row[1])
                reg1_region_list.append(row[3])
            elif row[3] == "South America":
                reg2_name_list.append(row[1])
                reg2_region_list.append(row[3])
            if row[11] == "Republic":
                gov1_name_list.append(row[1])
                gov1_govform_list.append(row[11])
            elif row[11] == "Monarchy":
                gov2_name_list.append(row[1])
                gov2_govform_list.append(row[11])
            if row[2] == "Europe":
                cont1_name_list.append(row[1])
                cont1_cont_list.append(row[2])
            elif row[2] == "Oceania":
                cont2_name_list.append(row[1])
                cont2_cont_list.append(row[2])
    regunion_names_list = reg1_name_list + reg2_name_list
    regunion_region_list = reg1_region_list + reg2_region_list
    govunion_names_list = gov1_name_list + gov2_name_list
    govunion_govform_list = gov1_govform_list + gov2_govform_list
    contunion_names_list = cont1_name_list + cont2_name_list
    contunion_cont_list = cont1_cont_list + cont2_cont_list
    unions_data_masterlist = [
        regunion_names_list,
        regunion_region_list,
        govunion_names_list,
        govunion_govform_list,
        contunion_names_list,
        contunion_cont_list,
    ]
    return unions_data_masterlist


def test_union_regions(unions_masterdata):
    """Asserts the equality of the dataframe of the union of North America and South America regions created through union operator using reframe library and the dataframe created from the list extracted from the csv file."""
    regions_union_data = {"name": unions_masterdata[0], "region": unions_masterdata[1]}
    df = pd.DataFrame(regions_union_data)
    assert (
        country.query('region == "North America"')
        .union(country.query('region == "South America"'))
        .project(["name", "region"])
        .reset_index(drop=True)
        .equals(df.reset_index(drop=True))
    )


def test_union_govforms(unions_masterdata):
    """Asserts the equality of the dataframe of the union of Republic and Monarchy government forms created through union operator using reframe library and the dataframe created from the list extracted from the csv file."""
    govforms_union_data = {
        "name": unions_masterdata[2],
        "governmentform": unions_masterdata[3],
    }
    df = pd.DataFrame(govforms_union_data)
    assert (
        country.query('governmentform == "Republic"')
        .union(country.query('governmentform == "Monarchy"'))
        .project(["name", "governmentform"])
        .reset_index(drop=True)
        .equals(df.reset_index(drop=True))
    )


def test_union_continents(unions_masterdata):
    """Asserts the equality of the dataframe of the union of Europe and Oceania continents created through union operator using reframe library and the dataframe created from the list extracted from the csv file."""
    continents_union_data = {
        "name": unions_masterdata[4],
        "continent": unions_masterdata[5],
    }
    df = pd.DataFrame(continents_union_data)
    assert (
        country.query('continent == "Europe"')
        .union(country.query('continent == "Oceania"'))
        .project(["name", "continent"])
        .reset_index(drop=True)
        .equals(df.reset_index(drop=True))
    )
