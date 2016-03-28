Feature: Resource-BigQuery integration

  Scenario Outline: Push/pull resource to BigQuery storage
    When We push/pull resource from "<dataset>" to BigQuery
    Then No errors are occured

    Examples: Datasets
        | dataset   |
        | synthetic |
