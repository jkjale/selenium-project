Feature: Sign up page functionality

  Scenario: User can create new account
    Given Open sign up page
    When Fill out the form
    And Click create account button
    Then User lands on main page and sees "Settings" link

