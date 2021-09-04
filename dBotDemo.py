from telegram.ext import CommandHandler, CallbackQueryHandler, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import YouTubeConnector
#import MoviesDB

Movies = ["Dear John", "Mama Mia"]
result = []
result2 = []



############################### Bot ############################################
def start(update, context):
    result.clear()
    update.message.reply_text(text="""\
                                    Hi there, I am ReWatch Bot.
                                    Welcome to the incredible Bot - ReWatch, which will help you decide what movie you want!. 
                                    based on your mood, or the genre - you will get all the details you need to pick a movie.
                                    So, just choose!
                                    """, reply_markup=type_choose_keyboard())


def type_choose(update, context):
    result.clear()
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=""""\
                                    Hi there, I am ReWatch Bot.
                                    Welcome to the incredible Bot - ReWatch, which will help you decide what movie you want!. 
                                    based on your mood, or the genre - you will get all the details you need to pick a movie.
                                    So, just choose!
                                    """,
                            reply_markup=type_choose_keyboard())


def genre(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please Pick a Genre", reply_markup=genre_keyboard())


def situation(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please Pick a Situation", reply_markup=situation_keyboard())


def action_genre(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="The action Movies", reply_markup=action_genre_keyboard())

def drama_genre(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="The action Movies", reply_markup=drama_genre_keyboard())

def friends_situation(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Watch With Friends", reply_markup=friends_situation_keyboard())

############################### KeyBoards ############################################
def type_choose_keyboard():
    keyboard = [
        [InlineKeyboardButton("Movie By Genre", callback_data='movie_by_genre')],
        [InlineKeyboardButton("Movie by Situation", callback_data='movie_by_situation')]
    ]
    return InlineKeyboardMarkup(keyboard)


def genre_keyboard():
    keyboard = [
        [InlineKeyboardButton("Action", callback_data='action_g')],
        [InlineKeyboardButton("Adventure", callback_data='adventure')],
        [InlineKeyboardButton("Animation", callback_data='animation')],
        [InlineKeyboardButton("Biography", callback_data='biography')],
        [InlineKeyboardButton("Crime", callback_data='crime')],
        [InlineKeyboardButton("Comedy", callback_data='comedy')],
        [InlineKeyboardButton("Drama", callback_data='drama_g')],
        [InlineKeyboardButton("Fantasy", callback_data='fantasy')],
        [InlineKeyboardButton("Family", callback_data='family')],
        [InlineKeyboardButton("History", callback_data='history')],
        [InlineKeyboardButton("Horror", callback_data='horror')],
        [InlineKeyboardButton("Music", callback_data='music')],
        [InlineKeyboardButton("Musical", callback_data='musical')],
        [InlineKeyboardButton("Romance", callback_data='romance')],
        [InlineKeyboardButton("Sci-Fi", callback_data='scifi')],
        [InlineKeyboardButton("Western", callback_data='western')],
        [InlineKeyboardButton("War", callback_data='war')],
        [InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')],
        [InlineKeyboardButton('Next - Find Movie', callback_data='find_movie')]
    ]
    return InlineKeyboardMarkup(keyboard)


def situation_keyboard():
    keyboard = [
        [InlineKeyboardButton("With Family", callback_data='w_family')],
        [InlineKeyboardButton("With Friends", callback_data='friends')],
        [InlineKeyboardButton("With Date", callback_data='w_date')],
        [InlineKeyboardButton("With MySelf", callback_data='w_myself')],
        [InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')]
    ]
    return InlineKeyboardMarkup(keyboard)


def action_genre_keyboard():
    for movie in Movies:
        result.append([InlineKeyboardButton(text=movie,
                                            url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(movie))])
    result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result)


def drama_genre_keyboard():
    #res = MoviesDB.MoviesDBWrapper.movies_by_genre(['Drama'])  # list of all the drama movies
    res = ['The GodFather', 'The Shawshank Redemption', 'The Dark Knight', "Schindler's List", "Goodfellas", "High and Low"]
    rating = [' - 9.4',' - 9,3', ' - 8,4', ' - 8.9', ' - 8.9',' - 8.7']
    for m,r in zip(res,rating):
        content = m + r
        result2.append([InlineKeyboardButton(text=content,
                                             url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(m))])
    result2.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result2)

def friends_situation_keyboard():
    res = ['Indiana Jones and the Last Crusade', 'Inside Out', 'Catch Me If You Can', 'Warrior']
    rating = [' - 8.2', ' - 8.1', ' - 8.1', ' - 8.1']
    for m,r in zip(res,rating):
        content = m+r
        result.append([InlineKeyboardButton(text = content,
                                             url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(m))])
    result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result)

############################# Handlers #########################################
updater = Updater('1951859494:AAGUJJUIT6uqvQFgOfnzCaYVMGG_YAN9qRM', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(type_choose, pattern='type'))
updater.dispatcher.add_handler(CallbackQueryHandler(genre, pattern='movie_by_genre'))
updater.dispatcher.add_handler(CallbackQueryHandler(situation, pattern='movie_by_situation'))
updater.dispatcher.add_handler(CallbackQueryHandler(action_genre, pattern="action_g"))
updater.dispatcher.add_handler(CallbackQueryHandler(drama_genre, pattern="drama_g"))
updater.dispatcher.add_handler(CallbackQueryHandler(friends_situation, pattern="friends"))
updater.start_polling()
