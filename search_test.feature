# Укажем что это за фича
Feature: Checking search
# У кажем имя сценария (в одной фиче может быть несколько)
  Scenario: Check some text in search results
# И используем наши шаги.
    Given website 'ya.ru'
    When search text 'Тест'
    And push button with text 'Найти'
    Then page include text 'Тест'