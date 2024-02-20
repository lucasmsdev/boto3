{"filter":false,"title":"batch_create_item.py","tooltip":"/python/dynamodb/batch_create_item.py","undoManager":{"mark":51,"position":51,"stack":[[{"start":{"row":0,"column":0},"end":{"row":60,"column":5},"action":"insert","lines":["with table.batch_writer() as batch:","    batch.put_item(","        Item={","            'account_type': 'standard_user',","            'username': 'johndoe',","            'first_name': 'John',","            'last_name': 'Doe',","            'age': 25,","            'address': {","                'road': '1 Jefferson Street',","                'city': 'Los Angeles',","                'state': 'CA',","                'zipcode': 90001","            }","        }","    )","    batch.put_item(","        Item={","            'account_type': 'super_user',","            'username': 'janedoering',","            'first_name': 'Jane',","            'last_name': 'Doering',","            'age': 40,","            'address': {","                'road': '2 Washington Avenue',","                'city': 'Seattle',","                'state': 'WA',","                'zipcode': 98109","            }","        }","    )","    batch.put_item(","        Item={","            'account_type': 'standard_user',","            'username': 'bobsmith',","            'first_name': 'Bob',","            'last_name':  'Smith',","            'age': 18,","            'address': {","                'road': '3 Madison Lane',","                'city': 'Louisville',","                'state': 'KY',","                'zipcode': 40213","            }","        }","    )","    batch.put_item(","        Item={","            'account_type': 'super_user',","            'username': 'alicedoe',","            'first_name': 'Alice',","            'last_name': 'Doe',","            'age': 27,","            'address': {","                'road': '1 Jefferson Street',","                'city': 'Los Angeles',","                'state': 'CA',","                'zipcode': 90001","            }","        }","    )"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":3},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":4},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["b"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["o"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["o"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["3"]}],[{"start":{"row":0,"column":12},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["d"]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["y"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["n"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["a"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["m"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["o"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["d"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["b"]}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":[" "],"id":6},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":[" "],"id":7}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["b"],"id":8},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["o"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["t"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["o"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["2"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["3"]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["3"],"id":9}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["2"],"id":10}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["3"],"id":11}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["3"],"id":12}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["."],"id":13}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["."],"id":14}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["3"],"id":15},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["."]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["r"]}],[{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"remove","lines":["r"],"id":16},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["."]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["."],"id":17},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["r"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["e"]},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["s"]},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["o"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["u"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["r"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["c"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["e"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["_"]}],[{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"remove","lines":["_"],"id":18}],[{"start":{"row":2,"column":25},"end":{"row":2,"column":27},"action":"insert","lines":["()"],"id":19}],[{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"remove","lines":[")"],"id":20},{"start":{"row":2,"column":26},"end":{"row":2,"column":28},"action":"insert","lines":["''"]}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"remove","lines":["'"],"id":21},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["d"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["u"]}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"remove","lines":["u"],"id":22},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"remove","lines":["d"]}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":29},"action":"insert","lines":["''"],"id":23}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":29},"action":"remove","lines":["''"],"id":24}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["d"],"id":25},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["y"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["n"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["a"]},{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["m"]},{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"insert","lines":["o"]},{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"insert","lines":["d"]},{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"insert","lines":["b"]},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["'"]}],[{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":[")"],"id":26}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"remove","lines":["'"],"id":27},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":[" "]},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"remove","lines":[")"]},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":["a"]},{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["s"]},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["d"]}],[{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"remove","lines":["d"],"id":28},{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"remove","lines":["s"]},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"remove","lines":["a"]},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"remove","lines":[" "]}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["'"],"id":29},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":[")"]}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["q"],"id":30}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"remove","lines":["q"],"id":31}],[{"start":{"row":2,"column":37},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["m"]},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["y"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["-"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["a"],"id":33},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["b"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["l"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["e"],"id":34},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"remove","lines":["l"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["b"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"remove","lines":["a"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"remove","lines":["t"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"remove","lines":["-"]}],[{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["_"],"id":35},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["t"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["a"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["v"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["b"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["l"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"remove","lines":["e"],"id":36},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["l"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"remove","lines":["b"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["v"]}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["b"],"id":37},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["l"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":[" "],"id":38},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":[" "],"id":39},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["r"]},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"remove","lines":["e"],"id":40},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":["r"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["b"],"id":41}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":["b"],"id":42}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["d"],"id":43},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["y"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["n"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["a"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["m"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["o"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["d"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["b"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":[";"]}],[{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"remove","lines":[";"],"id":44}],[{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["."],"id":45},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["T"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["a"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["b"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["l"]},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":25},"end":{"row":4,"column":27},"action":"insert","lines":["()"],"id":46}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":28},"action":"insert","lines":["''"],"id":47},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["1"]}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"remove","lines":["1"],"id":48},{"start":{"row":4,"column":26},"end":{"row":4,"column":28},"action":"remove","lines":["''"]}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":28},"action":"insert","lines":["''"],"id":49}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":8},"action":"remove","lines":["my_table"],"id":50},{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["t"]},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["a"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["b"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["l"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["e"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["r"],"id":51}],[{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["u"],"id":52},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["s"]},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["e"]},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["r"]},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":67,"column":5},"end":{"row":67,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1708451247211,"hash":"dc1af87e12cccb481ca478978a674f0424cac80f"}