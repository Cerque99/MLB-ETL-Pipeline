import os
from project import filter_and_process_games, export_summary_report, calculate_matchday_metrics

def test_filter_and_process_games():
    # We simulate a JSON from the MLB API with one completed game.
    mock_data = {
        "dates": [
            {
                "games": [
                    {
                        "status": {"abstractGameState": "Final"},
                        "teams": {
                            "home": {"team": {"name": "New York Yankees"}, "score": 5},
                            "away": {"team": {"name": "Boston Red Sox"}, "score": 3}
                        }
                    }
                ]
            }
        ]
    }
    result = filter_and_process_games(mock_data)
    assert len(result) == 1
    assert result[0]["home_team"] == "New York Yankees"
    assert result[0]["away_team"] == "Boston Red Sox"
    assert result[0]["home_score"] == 5
    assert result[0]["away_score"] == 3

def test_filter_and_process_games_no_games():
    empty_data = {"dates": []}
    result = filter_and_process_games(empty_data)
    assert result == []

def test_calculate_matchday_metrics():
    test_games = [
        {"home_team": "Team A", "away_team": "Team B", "home_score": 4, "away_score": 2},
        {"home_team": "Team C", "away_team": "Team D", "home_score": 1, "away_score": 3}
    ]
    analysis = calculate_matchday_metrics(test_games)

    assert analysis["total_games"] == 2
    assert analysis["total_runs"] == 10
    assert analysis["average_runs"] == 5.0
    assert "Team A" in analysis["highest_scoring_game"]

def test_export_summary_report():
    # Set up test data
    test_games = [
        {
            "home_team": "Los Angeles Dodgers",
            "away_team": "San Francisco Giants",
            "home_score": 4,
            "away_score": 2
        }
    ]

    test_analysis = {
        "total_games": 1,
        "total_runs": 6,
        "average_runs": 6.0,
        "highest_scoring_game": "San Francisco Giants vs Los Angeles Dodgers (6 carreras)"
    }

    file_name = export_summary_report("2024-07-01", test_games, test_analysis)

    #Verufy that the file was created successfully.
    assert os.path.exists(file_name)

    #Check that the content includes the expected data.
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Los Angeles Dodgers" in content
        assert "San Francisco Giants" in content
        assert "Average runs" in content

    #Clean up the generated test file.
    if os.path.exists(file_name):
        os.remove(file_name)
