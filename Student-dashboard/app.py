from dash import Dash

from src.utils.config_loader import load_config
from src.pipeline.load_data import load_data
from src.pipeline.features import create_features
from src.pipeline.scoring import compute_improvability

from src.dashboard.layout import layout
from src.dashboard.callbacks import register_callbacks


def run_pipeline():

    config = load_config()

    df = load_data(config["data"]["path"])
    df = create_features(df)
    df = compute_improvability(df, config)

    return df


df = run_pipeline()

app = Dash(__name__)
server = app.server

app.layout = layout
register_callbacks(app, df)

if __name__ == "__main__":
    app.run(debug=True)
