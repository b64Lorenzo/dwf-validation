from collections import defaultdict

from utils.filters import passes_filter
from utils.utils import transform_key


def collect(
    data,
    filters,
    group_by,
    dt_mode="ppp",
):
    """
    Group wave fields.
    """

    groups = defaultdict(list)

    for meta, field in data:

        if not all(
            passes_filter(
                meta.get(key),
                filters.get(key),
            )
            for key in filters
        ):
            continue

        grouping_key = (
            transform_key(
                meta,
                group_by,
                dt_mode=dt_mode,
            )
        )

        groups[
            grouping_key
        ].append(
            (
                meta,
                field,
            )
        )

    return dict(groups)