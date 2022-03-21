Feature: Search

  Scenario: Search movie by title
    Given index page is displayed
    When the user searches for movie by title "spiderman"
    And the user goes to Movie Category Search
    Then the user will see movie listing with some content
    And the movie listing contains phrase "Spider-Man" in any title
