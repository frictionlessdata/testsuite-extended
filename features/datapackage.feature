Feature: Datapackage operations

  # BigQuery

  Scenario Outline: Push/pull datapackage to BigQuery storage
    When We push/pull datapackage from "<dataset>" to BigQuery
    Then No errors are occured

    Examples: Datasets
        | dataset                      |
      # | country-codes                |
        | country-list                 |
      # | currency-codes               |
      # | gb-country-regional-analysis |
        | nasdaq-listings              |
        | testing                      |

  # SQL

  Scenario Outline: Push/pull datapackage to SQL storage
    When We push/pull datapackage from "<dataset>" to SQL
    Then No errors are occured

    Examples: Datasets
        | dataset                      |
      # | country-codes                |
        | country-list                 |
      # | currency-codes               |
        | gb-country-regional-analysis |
        | nasdaq-listings              |
        | testing                      |
