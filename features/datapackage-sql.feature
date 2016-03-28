Feature: Datapackage-SQL integration

  Scenario Outline: Push/pull datapackage to SQL storage
    When We push/pull datapackage from "<dataset>" to SQL
    Then No errors are occured

    Examples: Datasets
        | dataset                      |
        | country-list                 |
        | gb-country-regional-analysis |
        | nasdaq-listings              |
        | synthetic                    |
