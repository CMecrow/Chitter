from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

# Albums tests

# def test_get_albums(db_connection, web_client):
#     db_connection.seed('seeds/record_store.sql')
#     get_response = web_client.get("/albums")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == ""\
#         "Album(1, Silent Alarm, 2005, 1)"

# def test_post_album(db_connection, web_client):
#     db_connection.seed('seeds/record_store.sql')
#     post_response = web_client.post("/albums", data={
#         'title': 'Watch Out',
#         'release_year': '2004',
#         'artist_id': '2'})
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == ''

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == ""\
#         "Album(1, Silent Alarm, 2005, 1)\n"\
#         "Album(2, Watch Out, 2004, 2)"
    
# # Artists tests

# def test_get_artists(db_connection, web_client):
#     db_connection.seed('seeds/record_store.sql')
#     get_response = web_client.get("/artists")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == ""\
#         "Artist(1, Bloc Party, Indie)"
    
# def test_post_artist(db_connection, web_client):
#     db_connection.seed('seeds/record_store.sql')
#     post_response = web_client.post("/artists", data={
#         'name': 'The Wombats',
#         'genre': 'Indie'})
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == ''

#     get_response = web_client.get('/artists')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == ""\
#         "Artist(1, Bloc Party, Indie)\n"\
#         "Artist(2, The Wombats, Indie)"

# """
# We can get an emoji from the /emoji page
# """
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    first_album = page.locator("h2")
    expect(first_album).to_have_text('Silent Alarm')

def test_get_album(db_connection, page, test_web_address):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Silent Alarm")
    album_name = page.locator(".t-title")
    expect(album_name).to_have_text("Title: Silent Alarm")

def test_create_album(db_connection, page, test_web_address):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.fill("input[name='title']", "Copper Gone")
    page.fill("input[name='release_year']", "2010")
    page.fill("input[name='artist_id']", "6")
    page.click("text=Create Album")
    new_addition = page.locator("text=Copper Gone")
    expect(new_addition).to_have_text("Copper Gone")

def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Create Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release Year can't be blank, Artist id can't be blank")

def test_delete_album(db_connection, page, test_web_address):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.fill("input[name='title']", "Copper Gone")
    page.fill("input[name='release_year']", "2010")
    page.fill("input[name='artist_id']", "6")
    page.click("text=Create Album")
    page.click("text=Copper Gone")
    page.click("text=Delete Album")
    album_list = page.locator(".albums_list")
    expect(album_list).not_to_have_text("Copper Gone")

