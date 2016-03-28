Feature: Datapackage operations

  Scenario Outline: Push/pull datapackage to BigQuery storage
    When We push/pull datapackage from "<dataset>" to BigQuery
    Then No errors are occured

    Examples: Datasets
        | dataset      |
        | testing      |

  Scenario Outline: Push/pull datapackage to SQL storage
    When We push/pull datapackage from "<dataset>" to SQL
    Then No errors are occured

    Examples: Datasets
        | dataset      |
        | country-list |
        | testing      |
