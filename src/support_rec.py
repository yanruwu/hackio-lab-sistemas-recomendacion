import matplotlib.pyplot as plt
import seaborn as sns

def get_recs_content(df_similarity, title, n_recs=5, plot=True):
    """
    Generate content-based recommendations based on similarity scores.

    Parameters
    ----------
    df_similarity : pandas.DataFrame
        A DataFrame containing similarity scores, where rows and columns correspond to item titles.
    title : str
        The title of the item for which recommendations are to be generated.
    n_recs : int, optional
        The number of top recommendations to return, by default 5.
    plot : bool, optional
        Whether to display a bar plot of the top recommendations, by default True.

    Returns
    -------
    pandas.Series
        A Series containing the top `n_recs` recommendations, with similarity scores as values and titles as indices.

    Examples
    --------
    >>> df_similarity = pd.DataFrame({
    ...     "Item A": [1.0, 0.9, 0.3],
    ...     "Item B": [0.9, 1.0, 0.5],
    ...     "Item C": [0.3, 0.5, 1.0]
    ... }, index=["Item A", "Item B", "Item C"])
    >>> get_recs_content(df_similarity, "Item A", n_recs=2, plot=False)
    Item B    0.9
    Item C    0.3
    dtype: float64
    """
    top_recs = df_similarity[title].sort_values(ascending = False)[1:].head(n_recs)
    if plot:
        plt.figure(figsize = (10,6))
        plt.grid(ls = "--", lw = 0.6)
        sns.barplot(x = top_recs, y = top_recs.index, palette = "mako")
        plt.title(f"Top {n_recs} Recommendations if you liked {title}")
        plt.xlabel("")
        plt.show()
    return top_recs

def get_recs_genre(liked_genre, df_genres, priority="rating", n_recs=10):
    """
    Get recommendations for games of a specific genre based on the chosen priority.

    Parameters
    ----------
    liked_genre : str
        The genre for which recommendations are to be retrieved.
    df_genres : pandas.DataFrame
        The dataframe containing game information. Must include the columns:
        - 'genre': The genre of the games.
        - 'overall_player_rating': The overall player rating of the games.
        - 'number_of_english_reviews': The number of English reviews for the games.
    priority : str, optional
        The sorting priority for recommendations. Can be:
        - "rating" (default): Sort recommendations by overall player rating (descending).
        - "n_reviews": Sort recommendations by the number of English reviews (descending).
    n_recs : int, optional
        The number of recommendations to retrieve. Default is 10.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing up to `n_recs` games of the specified genre,
        sorted by the specified priority.

    Examples
    --------
    >>> get_recs_genre("Action", df, priority="rating", n_recs=5)
    >>> get_recs_genre("Adventure", df, priority="n_reviews", n_recs=15)

    Notes
    -----
    - If `liked_genre` is not present in `df_genres`, the function will return an empty dataframe.
    - The function does not handle ties in sorting explicitly; games with equal values
      for the priority field will appear in their original order.

    """

    df_recs = df_genres[df_genres["genre"] == liked_genre].head(n_recs)
    if priority == "rating":
        return df_recs.sort_values(by = "overall_player_rating", ascending = False)
    elif priority == "n_reviews":
        return df_recs.sort_values(by = "number_of_english_reviews", ascending = False)