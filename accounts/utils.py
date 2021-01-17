def sum_and_order(items, thres=5):

    # summing the values
    tally = {}
    for exp in items:
        if exp.cat not in tally:
            tally[exp.cat] = exp.price
        else:
            tally[exp.cat] += exp.price

    # listing the highest values
    values = sorted(tally.items(), reverse=True, key=lambda amt: amt[1])
    if len(values) > thres:
        others = sum([i[1] for i in values[thres - 2:]])
        values = values[:thres - 1]
        values.append(('others', others))
    return dict(values)
