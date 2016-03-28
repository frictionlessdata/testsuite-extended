Feature: Resource-SQL integration

  Scenario Outline: Push/pull resource to SQL storage
    When We push/pull resource from "<dataset>" to SQL
    Then No errors are occured

    Examples: Datasets
        | dataset   |
        | synthetic |
