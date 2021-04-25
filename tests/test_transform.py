from json2csv.transform import flatten_data, extract_data

def test_extract_data():
    test_cases = [
        {'case': {
            'results': [
                {'key1': 'val1'},
                {'key2': 'val2'},
                {'key3': 'val3'},
            ]
        },
        'datakey': 'results',
        'expected': [
            {'key1': 'val1'},
            {'key2': 'val2'},
            {'key3': 'val3'},
        ]},
        {'case': [
            {'data': [1, 2, 3]},
            {'data': [4, 5, 6]},
            {'data': [7, 8, 9]},
        ],
        'datakey': 'data',
        'expected': [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]}
    ]

    for test_case in test_cases:
        result = extract_data(test_case['case'], test_case['datakey'])

        assert test_case['expected'] == result


def test_flatten_data():
    test_cases = [
        {'case': [
            {'a': {'b': 1, 'c': 2}},
            {'x': {'y': 5, 'z': 8}}
        ],
        'expected': [
            {'a_b': 1, 'a_c': 2},
            {'x_y': 5, 'x_z': 8},
        ]},
        {'case': {
            'top': {
                'middle': {
                    'bottom': {
                        'one': 1,
                        'two': 2,
                        'three': 3
                    }
                }
            }
        },
        'expected': {
            'top_middle_bottom_one': 1,
            'top_middle_bottom_two': 2,
            'top_middle_bottom_three': 3,
        }}
    ]

    for test_case in test_cases:
        result = flatten_data(test_case['case'])

        assert test_case['expected'] == result
