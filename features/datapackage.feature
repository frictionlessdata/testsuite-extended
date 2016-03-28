Feature: Datapackage core and integrations work

  Scenario Outline: Push/pull datapackage to SQL storage
    When We push/pull datapackage from "<path>" to SQL
    Then No errors are occured

    Examples: Synthetic
        | path             |
        | datasets/testing |
