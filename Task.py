class Task():
    isRunning = False
    names = [
        ['лучшие', 'лучшее', 'топ'],
        ['всё', 'всё подряд', 'all']
    ]
    filters = [
        ['сутки', 'неделя', 'месяц'],
        ['без порога', '10', '25', '50', '100']
    ]
    filters_code_names = [
        ['daily', 'weekly', 'monthly'],
        ['all', 'top10', 'top25', 'top50', 'top100']
    ]
    mySource = ''
    myFilter = ''
    def __init__(self):
        return