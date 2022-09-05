#Constants:
MAX_LEN = 50
EMPTY_STR = ""

class LogSubmission (object):
    # Instance Members
    activity_done = EMPTY_STR
    activity_length = 0
    fun = EMPTY_STR
    rating = 0
    #static variable
    streak_counter = 1

    # Parametrized Constructor
    def __init__(self, activity_done, activity_length, fun, rating):
        self.set_activity_done(activity_done)
        self.set_activity_length(activity_length)
        self.set_fun(fun)
        self.set_rating(rating)
        self.streak_counter += 1

    # Set Activity Done
    def set_activity_done(self, activity_done):
        if self.str_ok(activity_done):
            self.activity_done = activity_done
            return True
        self.activity_done = EMPTY_STR
        return False

    # Set Fun
    def set_fun(self, fun):
        if self.str_ok(fun):
            self.activity_done = fun
            return True
        self.fun = EMPTY_STR
        return False

    # Set Activity Length
    def set_activity_length(self, activity_length):
        self.activity_length = activity_length
        return True

    # Get Rating
    def set_rating(self, rating):
        self.rating = rating
        return True

    # Get Rating
    def get_activity_done(self):
        return self.activity_done

    # Get Rating
    def get_activity_length(self):
        return self.activity_length

    def get_fun(self):
        return self.fun

    def get_rating(self):
        return self.rating

    def get_streak_counter(self):
        return self.streak_counter

    #validating the demo file
    def str_ok(self, the_str):
        if not the_str.isprintable():
            return False
        return True
