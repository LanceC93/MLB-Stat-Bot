#This agent retrieves quantitative stats from a stats api
from langchain.tools import tool
from lanchain.chat_models import init_chat_model
from state import ResearchState
from config import MODEL_PROVIDER, MODEL, OLLAMA_BASE_URL
import operator
import statsapi
import json

model = init_chat_model(
    MODEL,
    model_provider= MODEL_PROVIDER,
    temperature = 0,
    base_url= OLLAMA_BASE_URL
)

@tool
def get_player_stats(player_name: str, stat_type: str = "season") -> dict:
    """
    Fetches MLB player statistics.
    
    Args:
        player_name (str): The player's full or partial name.
        stat_type (str): The scope of stats to retrieve. 
                          Options: 'season' (current year), 
                                   'career' (lifetime totals), 
                                   'yearByYear' (historical breakdown).
    """
    results = statsapi.lookup_player(player_name)
    if not results:
        return {"error": f"No player found"}

    player_id = results[0]['id']
    return json.dumps(statsapi.player_stat_data(player_id, type=stat_type), indent=2)


