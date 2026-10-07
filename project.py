import sys
import requests

def main():
    print("--- MLB Statistics and Analytics Pipeline ---")
    date = input("Enter a date (format YYYY-MM-DD, e.g., 2026-04-01): ")

    try:
        raw_data = get_mlb_data(date)
        processed_games = filter_and_process_games(raw_data)

        if not processed_games:
            print("No completed games found for the specified date. ")
            return

        # Analyze additional metrics from the processed data
        analysis = calculate_matchday_metrics(processed_games)

        export_summary_report(date, processed_games, analysis)
        print("Analytical report successfully generated in 'mlb_report.txt'!")

    except requests.RequestException:
        sys.exit("Connection error while attempting to access the MLB API.")
    except ValueError as e:
        sys.exit(f"Data error: {e}")


def get_mlb_data(date):
    """
    Function 1: Makes the HTTP request to the public MLB API
    to get the schedule and results for a specific date;
    """
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={date}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def filter_and_process_games(json_data):
    """
    Function 2: Processes the raw JSON, extracts the played games,
    and collects key info about teams and scores.
    """
    clean_games = []

    dates = json_data.get("dates", [])
    if not dates:
        return clean_games

    games = dates[0].get("games", [])
    for game in games:
        #Inspext the exact status of each game
        status = game.get("status", {}).get("abstractGameState", "")
        #Process only completed games
        if "final" in status.lower() or "completed" in status.lower():
            teams = game.get("teams", {})
            home_team = teams.get("home", {}).get("team", {}).get("name", "Desconocido")
            away_team = teams.get("away", {}).get("team", {}).get("name", "Desconocido")
            home_score = teams.get("home", {}).get("score", 0)
            away_score = teams.get("away", {}).get("score", 0)

            clean_games.append({
                "home_team": home_team,
                "away_team": away_team,
                "home_score": home_score,
                "away_score": away_score
            })

    return clean_games


def calculate_matchday_metrics(games):
    """
    Function 3: Calculates aggregated statistics for the matchday, such as
    total runs scored and the game with the highest offense.
    """
    if not games:
        return {}
    total_runs = 0
    max_game_runs = -1
    highest_scoring_game = ""

    for g in games:
        game_runs = g["home_score"] + g["away_score"]
        total_runs += game_runs

        if game_runs > max_game_runs:
            max_game_runs = game_runs
            highest_scoring_game = f"{g['away_team']} vs {g['home_team']} ({game_runs} runs)"

    average_runs = total_runs / len(games)

    return {
        "total_games": len(games),
        "total_runs": total_runs,
        "average_runs": round(average_runs, 2),
        "highest_scoring_game": highest_scoring_game
    }

def export_summary_report(date, games, analysis):
    """
    Function 4: Generates a structured text file summarizing
    the matchups and the calculated metrics.
    """

    file_name = "mlb_report.txt"
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write(f"        MLB MATCHDAY REPORT - {date}           \n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Total games analyzed: {analysis['total_games']}\n")
        f.write(f"Total runs scored: {analysis['total_runs']}\n")
        f.write(f"Average runs per game: {analysis['average_runs']}\n\n")

        f.write(f"Most offensive game: {analysis['highest_scoring_game']}\n\n")


        f.write("=" * 60 + "\n")
        f.write("MATCHUP DETAILS:\n")
        f.write("=" * 60 + "\n\n")

        for g in games:
            line = f"-{g['away_team']} ({g['away_score']}) @ {g['home_team']} ({g['home_score']})\n"
            f.write(line)

    return file_name

if __name__ == "__main__":
    main()




