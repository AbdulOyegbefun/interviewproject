import pickle 
header = ["level",'lang','tweets','phd']
interview_tree = \
["Attribute", "level",
    ["Value", "Senior",
        ["'Attribute", "tweets",
            ["Value", "yes",
                ["Leaf", "True", 2, 5]
            ],
            ["Value", "no",
                ["Leaf", "False", 3, 5]
            ]
        ]
    ],
    ["Value", "Mid",
        ["Leaf", "True", 4, 14]
    ],
    ["Value", "Junior",
        ["Attribute", "phd",
            ["Value", "yes",
                ["Leaf", "False", 2, 5]
            ],
            ["Value", "no",
                ["Leaf", "True", 3, 5]
            ]
        ]
    ]
]

packaged_object = [header, interview_tree]

outfile = open('tree.p','wb')
pickle.dump(packaged_object,outfile)
outfile.close()
