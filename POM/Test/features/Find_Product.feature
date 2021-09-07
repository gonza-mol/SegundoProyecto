Feature: Execute a search for a product, through the search engine
  As a logged in user,
  I want to be able to search for a desired product, using the search engine.

@Regression
  Scenario: Search for a product, through the search engine
    Given I am on login in the Automation test store page, and I want to search for a certain product
    When I type the "French" to search in the search engine, and I execute the search
    Then I get a product "French" and verify that it is the desired product