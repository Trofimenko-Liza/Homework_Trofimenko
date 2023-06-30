import requests
import json

create_product_url = 'https://api.restful-api.dev/objects'

restful_url = 'https://api.restful-api.dev/objects'

product_headers = {
    "content-type": "application/json"
}

product_json = json.dumps({
    "name": "Apple MacBook Pro 16",
    "data":{
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
})

product_json2 = json.dumps({
    "name": "Apple MacBook Pro 16",
    "data":{
        "year": 2020,
        "price": 1849.99,
        "CPU model": "Intel Core i7",
        "Hard disk size" : "1 TB",
        "display": "17"
    }
})



#test_url = 'https://api.restful-api.dev/objects/ff80818188764f13018877da84a601a1'
#post_a_product = requests.post(create_product_url, data=product_json, headers=product_headers)
#print(post_a_product.json())

#view_a_product = requests.get(test_url, data=product_json2, headers=product_headers)
#test_url = 'https://api.restful-api.dev/objects/ff80818188764f13018877da84a601a1'

#put_a_product = requests.put(test_url, data=product_json2, headers=product_headers)
#print()


patch_json = json.dump({
    "name": "Apple MacBook Pro 16 (Update Name)"
})

patch_product = requests.patch(f"{restful_url}/ff80818188764f13018877e09ef601a9", headers=product_headers, data =patch_json)
print(patch_product.content)

test_url = 'https://api.restful-api.dev/objects/ff80818188764f13018877e09ef601a9'

del_a_product_2 = requests.delete(test_url)