from behave import given, when, then

import pages


@given('index page is displayed')
def step_impl(context):
    context.index_page = pages.IndexPage(context.driver)
    context.index_page.visit()


@when('the user searches for movie by title "{text}"')
def step_impl(context, text):
    context.main_results_page = context.index_page.search(text)


@when('the user goes to Movie Category Search')
def step_impl(context):
    context.movie_results_page = context.main_results_page.go_to_movie_titles()


@then('the user will see movie listing with some content')
def step_impl(context):
    assert not context.movie_results_page.is_listing_empty()


@then('the movie listing contains phrase "{text}" in any title')
def step_impl(context, text):
    assert context.movie_results_page.is_phrase_in_any_movie_title(text)
