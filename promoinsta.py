from instapy import InstaPy
from instapy.util import smart_run, tags_string_to_list

# insta_username = 'drawwer'
# insta_password = 'warandpiece'
insta_username='mankos.tattoo'
insta_password='10011964A'

insta_tags = ['']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

with smart_run(session):
    # Stage 2 - work with competitor followers
    # session.set_do_like(enabled=True, percentage=100)
    # session.set_locations(['Moscow', 'Moscow, Russia'])
    # session.set_location_limits('Moscow', 10)


    print(tags_string_to_list(session.user_tags))
    print(tags_string_to_list(session.user_tags)[0])
    print(tags_string_to_list(session.user_tags)[1])
    # session.get_competitor_users_by_tags(tags_string_to_list(session.user_tags)[0], amount=10)

    # print(session.competitor_users, session.competitor_users_count)

    
    # Выставляем границы для пользователей
    # session.set_relationship_bounds(enabled=True,
    #                                 potency_ratio=None,
    #                                 delimit_by_numbers=True,
    #                                 max_followers=6000,
    #                                 max_following=3000,
    #                                 min_followers=30,
    #                                 min_following=30)
    # session.set_user_interact(amount=2, randomize=True, percentage=30,
    #                           media='Photo')
    
    # session.set_do_comment(enabled=True, percentage=5)
    # session.set_comments(
    #     ['Nice shot! @{}', 'I love your profile! @{}', '@{} Love it!',
    #      '@{} :heart::heart:',
    #      '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
    #     media='Photo')

    # unfollow activity
    # session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM",
    #                        unfollow_after=42 * 60 * 60, sleep_delay=300)

    # follow activity
    # ammount_number = 500
    # session.follow_user_followers(['chrisburkard', 'danielkordan'],
    #                               amount=ammount_number, randomize=False,
    #                               interact=True, sleep_delay=240)
    

    # session.follow_by_tags(['Moscow'], amount=10)