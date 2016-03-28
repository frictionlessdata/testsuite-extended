Feature: Datapackage integrations

  Scenario Outline: Push/pull datapackage to storage
    When We push/pull datapackage from "<dataset>" to <backend>
    Then No errors are occured

    Examples: BigQuery
        | backend  | dataset                      |
        | BigQuery | country-codes                |
        | BigQuery | country-list                 |
        | BigQuery | currency-codes               |
        | BigQuery | gb-country-regional-analysis |
      # | BigQuery | gdp                          |
        | BigQuery | language-codes               |
        | BigQuery | nasdaq-listings              |
        | BigQuery | registry                     |
        | BigQuery | s-and-p-500-companies        |
        | BigQuery | synthetic                    |

    Examples: SQL
        | backend  | dataset                      |
        | SQL      | country-codes                |
        | SQL      | country-list                 |
        | SQL      | currency-codes               |
        | SQL      | gb-country-regional-analysis |
     #  | SQL      | gdp                          |
        | SQL      | language-codes               |
        | SQL      | nasdaq-listings              |
        | SQL      | registry                     |
        | SQL      | s-and-p-500-companies        |
        | SQL      | synthetic                    |
