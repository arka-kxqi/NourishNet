from kybra import Opt, nat, Record, query, update, Vec, void, nat64, StableBTreeMap

class FoodLedger(Record):
    name: str
    address: str
    city: str
    zipcode: str
    phone: str
    completed: bool
    delete: bool

FoodLedgers = StableBTreeMap[nat, FoodLedger](memory_id=3, max_key_size=1_000, max_value_size=1_000)

#sample data:
# FoodLedgers.insert(0, {"name": "Allan Gardens Food Bank",
#     "address": "353 Sherbourne St",
#     "city": "Toronto",
#     "zipcode": "M5A 2S3",
#     "phone": "416-604-5788",
#     "completed": True,
#     "delete": False
#     })
# FoodLedgers.insert(1, {"name": "Bethany Baptist Church Food Bank",
#     "address": "1041 Pape Ave",
#     "city": "Toronto",
#     "zipcode": "M4K 3W1",
#     "phone": "647-366-9041",
#     "completed": False,
#      "delete": False})


next_id: nat = max(FoodLedgers.keys())+1

@query
def f1_show_all_FoodLedgers() -> str:
    output = "\n___Food Bank List___"
    for idx, FoodLedger_entry in FoodLedgers.items():
        if not FoodLedger_entry["delete"]:
            output += f'\n{idx} : ' + f' {FoodLedger_entry["name"]}' + f' {FoodLedger_entry["address"]}' +f' {FoodLedger_entry["city"]}' +f' {FoodLedger_entry["zipcode"]}' +f' {FoodLedger_entry["phone"]}'
            if FoodLedger_entry["completed"]:
                output += " ✔"
    return output

@update
def f2_add_FoodLedger( val: FoodLedger) -> nat:

    global next_id
    id = next_id
    FoodLedgers.insert(next_id, val)
    next_id += 1
    return id

@query
def f3_search_FoodLedgers(zipcode: str) -> str:
    search_items = {key: FoodLedger for key, FoodLedger in FoodLedgers.items() if zipcode in FoodLedger["zipcode"]}
    output = "\n___Food Bank List___"
    for FoodLedger_entry in search_items.values():
        if not FoodLedger_entry["delete"]:
            output += f'\n{FoodLedger_entry["name"]}' + f' {FoodLedger_entry["address"]}' +f' {FoodLedger_entry["city"]}' +f' {FoodLedger_entry["zipcode"]}' +f' {FoodLedger_entry["phone"]}'
            if FoodLedger_entry["completed"]:
                output += " ✔"
    return output

@update
def f4_delete_FoodLedger( key: nat) -> nat:
    item = FoodLedgers.get(key)
    item['delete'] = True
    FoodLedgers.insert(key, item)
    return key

@query
def f5_get_FoodLedgers_by_id(key: nat) -> Opt[FoodLedger]:
    return FoodLedgers.get(key)

@query
def f6_get_all_FoodLedgers() -> Vec[FoodLedger]:
    return FoodLedgers.values()
