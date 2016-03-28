Feature: Datapackage-BigQuery integration

  Scenario Outline: Push/pull datapackage to BigQuery storage
    When We push/pull datapackage from "<dataset>" to BigQuery
    Then No errors are occured

    Examples: Datasets
        | dataset                      |
        | country-list                 |
        | nasdaq-listings              |
        | synthetic                    |
