import unittest
from scripts.basic_filtering import PlayerFilter  

class TestPlayerFilter(unittest.TestCase):
    """
    class to test the dataset input in different ways
    """

    def test_filter_players_over_age(self):
        """Test para verificar el filtrado por edad."""
        result = self.player_filter.filter_players_over_age(30)
        self.assertTrue(all(player['age'] > 30 for index, player in result.iterrows()))

    def test_filter_by_club(self):
        """Test para verificar el filtrado por club."""
        club_name = 'Bayern Munich'
        result = self.player_filter.filter_by_club(club_name)
        self.assertTrue(all(player['club'] == club_name for index, player in result.iterrows()))

    def test_filter_by_nationality(self):
        """Test para verificar el filtrado por nacionalidad."""
        nationality = 'Germany'
        result = self.player_filter.filter_by_nationality(nationality)
        self.assertTrue(all(player['nationality'] == nationality for index, player in result.iterrows()))
    
    def test_filter_players_by_nonexistent_age(self):
        """Test para verificar el filtrado por una edad que no existe."""
        result = self.player_filter.filter_players_over_age(100)
        self.assertEqual(len(result), 0)

    def test_filter_by_nonexistent_club(self):
        """Test para verificar el filtrado por un club inexistente."""
        result = self.player_filter.filter_by_club('Fantasy FC')
        self.assertEqual(len(result), 0)

    def test_filter_by_nonexistent_nationality(self):
        """Test para verificar el filtrado por una nacionalidad inexistente."""
        result = self.player_filter.filter_by_nationality('Atlantis')
        self.assertEqual(len(result), 0)

    def test_filter_players_within_age_range(self):
        """Test para verificar el filtrado dentro de un rango de edad."""
        result = self.player_filter.filter_players_within_age_range(25, 30)
        self.assertTrue(all(25 <= player['age'] <= 30 for index, player in result.iterrows()))

    def test_filter_by_club_case_insensitivity(self):
        """Test para verificar el manejo de mayúsculas y minúsculas en el nombre del club."""
        result_upper = self.player_filter.filter_by_club('BAYERN MUNICH')
        result_lower = self.player_filter.filter_by_club('bayern munich')
        self.assertEqual(len(result_upper), len(result_lower))

    def test_filter_on_empty_dataframe(self):
        """Test para verificar el filtrado en un DataFrame vacío."""
        self.player_filter.data = pd.DataFrame()
        result = self.player_filter.filter_players_over_age(30)
        self.assertTrue(result.empty)

    def test_filter_when_dataframe_is_none(self):
        """Test para verificar la respuesta cuando el DataFrame es None."""
        self.player_filter.data = None
        result = self.player_filter.filter_players_over_age(30)
        self.assertIsNone(result)


if __name__ == '_main_':
    unittest.main()