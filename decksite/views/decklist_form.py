from decksite.views.league_form import LeagueForm


# pylint: disable=no-self-use
class DecklistForm(LeagueForm):
    def __init__(self, form, person_id) -> None:
        super().__init__(form)
        self.person_id = person_id
        self.classify_illegal_cards()

    def classify_illegal_cards(self) -> None:
        if self.form.card_errors is not None:
            self.has_not_legal = 'Legality_Not_Legal' in self.form.card_errors and len(self.form.card_errors['Legality_Not_Legal']) > 0
            self.has_banned = 'Legality_Banned' in self.form.card_errors and len(self.form.card_errors['Legality_Banned']) > 0
            self.has_bugs = 'Legality_Bugs' in self.form.card_errors and len(self.form.card_errors['Legality_Bugs']) > 0
            self.has_too_many = 'Legality_Too_Many' in self.form.card_errors and len(self.form.card_errors['Legality_Too_Many']) > 0
