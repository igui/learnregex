import string

from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _

from ..utils import get_random_string, load_solution_function


class Adventure(BaseAdventure):

    title = _('Special characters')
    dictionary = string.ascii_lowercase + string.digits

    def test(self, file):
        function = load_solution_function(file)
        correct_argument = '{}\{}'.format(
            get_random_string(self.dictionary, 0, 5),
            get_random_string(self.dictionary, 0, 5)
        )
        if not function(correct_argument):
            raise AdventureVerificationError(
                _("Your function didn't return True when executed with a "
                  "correct argument '{}'.".format(correct_argument))
            )
        wrong_argument = get_random_string(self.dictionary, 1, 5)
        if function(wrong_argument):
            raise AdventureVerificationError(
                _("Your function returned True when executed with a wrong "
                  "argument '{}'.".format(wrong_argument)))
