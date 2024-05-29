def preprocess_input_data(input_data):
    return input_data / 255.0

topeng_bali_array =['Topeng Bujuh','Topeng Dalem','Topeng Keras','Topeng Penasar','Topeng Sidakarya','Topeng Tua','Topeng Wijil']

products = {
    "error":"false",
    "message":"success",
    "topeng":[
        {
            "id":1,
            "image-url":"https://storage.googleapis.com/kultura-image/topeng-bujuh.png",
            "informasi":"Topeng spesialis lucu di antara topeng Bali lainnya seperti topeng tua dan topeng keras",
            "name":"Topeng Bujuh"
        },
        {
            "id":2,
            "image-url":"https://storage.googleapis.com/kultura-image/topeng-dalem.jpeg",
            "informasi":"Topeng Dalem Arsa Wijaya berwajah manis pada Topeng Wali, melambangkan pemimpin yang membawa harapan (arsa) dan kemenangan (wijaya) bagi rakyatnya. Topeng Arsa Wijaya Secara visual, rupa topeng ini berwajah tampan, bermata sipit, memakai urna, dominan berwarna putih.",
            "name":"Topeng Dalem Arsa Wijaya"
        },
        {
            "id":3,
            "image-url":"https://storage.googleapis.com/kultura-image/topeng-keras.jpg",
            "informasi":"Topeng keras biasa lebih dikenal sebagai sosok petarung.",
            "name":"Topeng Keras"
        },
        {
            "id":4,
            "image-url":"https://storage.googleapis.com/kultura-image/topeng-penasar.jpg",
            "informasi":"tokoh penasar (penutur cerita)",
            "name":"Topeng Penasar"
        },
        {
            "id":5,
            "image-url": "https://storage.googleapis.com/kultura-image/topeng-sidakarya-1.jpeg",
            "informasi":"Topeng berasal dari kata tup yang artinya tutup. Sidakarya berasal dari kata \"sida\" yang artinya mencapai, dan \"karya\" yang artinya tujuan atau pekerjaan. Sidakarya memiliki makna mencapai tujuan atau menyelesaikan pekerjaan",
            "name":"Topeng Sidakarya"
        },
        {
            "id":6,
            "image-url": "https://storage.googleapis.com/kultura-image/topeng-tua-1.jpg",
            "informasi":"Topeng tua biasanya digunakan dalam pentas seni dalam ritual peringatan piodalan.",
            "name":"Topeng Tua"
        },
        {
            "id":7,
            "image-url":"https://storage.googleapis.com/kultura-image/topeng-wijil.jpeg",
            "informasi":"Karkater wijil merupakan karakter punakawan yang perpasangan dengan Penasar. Mereka adalah pendamping atau abdi raja dalam kesenian topeng wali",
            "name":"Topeng Wijil"
        }
    ],
    "event":[
        {
            "id":1,
            "image-url":"https://storage.googleapis.com/kultura-image/event-1.jpg",
            "name":"Tari Kecak",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":2,
            "image-url":"https://storage.googleapis.com/kultura-image/event-2.jpg",
            "name":"Tari Puspanjali",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":3,
            "image-url":"https://storage.googleapis.com/kultura-image/event-3.jpg",
            "name":"Tari Baris",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":4,
            "image-url":"https://storage.googleapis.com/kultura-image/event-4.jpg",
            "name":"Tari Legong",
            "informasi":"Pentas Seni Topeng Bali"
        }
        {
            "id":5,
            "image-url":"https://storage.googleapis.com/kultura-image/event-5.jpg",
            "name":"Tari Barong",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":6,
            "image-url":"https://storage.googleapis.com/kultura-image/event-6.jpg",
            "name":"Tari Joged Bumbung",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":7,
            "image-url":"https://storage.googleapis.com/kultura-image/event-7.jpg",
            "name":"Tari Rejang Dewa",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":8,
            "image-url":"https://storage.googleapis.com/kultura-image/event-8.jpg",
            "name":"Tari Kupu-Kupu Tarum",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":9,
            "image-url":"https://storage.googleapis.com/kultura-image/event-9.jpg",
            "name":"Tari Cendrawasih",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":10,
            "image-url":"https://storage.googleapis.com/kultura-image/event-10.jpg",
            "name":"Tari Janger",
            "informasi":"Pentas Seni Topeng Bali"
        },
        {
            "id":11,
            "image-url":"https://storage.googleapis.com/kultura-image/event-11.jpg",
            "name":"Tari Pendet",
            "informasi":"Pentas Seni Topeng Bali"
        },
    ],
    "workshop":[
        {
            {
                "id": 1,
                "image-url": "https://storage.googleapis.com/kultura-image/workshop-1.jpg",
                "name": "Mask Making Workshop",
                "informasi": "Join our workshop to learn the art of creating traditional Balinese masks. Explore different techniques and materials used in mask making.",
                "date": "2022-10-15",
                "time": "10:00 AM - 12:00 PM",
                "location": "Kultura Art Studio"
            },
            {
                "id": 2,
                "image-url": "https://storage.googleapis.com/kultura-image/workshop-2.jpg",
                "name": "Batik Painting Workshop",
                "informasi": "Join our workshop to learn the art of traditional Batik painting. Discover the intricate patterns and vibrant colors of Batik.",
                "date": "2022-11-05",
                "time": "2:00 PM - 4:00 PM",
                "location": "Kultura Art Studio"
            },
            {
                "id": 3,
                "image-url": "https://storage.googleapis.com/kultura-image/workshop-3.jpg",
                "name": "Wood Carving Workshop",
                "informasi": "Join our workshop to learn the art of traditional Balinese wood carving. Experience the craftsmanship and create your own wooden masterpiece.",
                "date": "2022-12-10",
                "time": "9:00 AM - 12:00 PM",
                "location": "Kultura Art Studio"
            },
            {
                "id": 4,
                "image-url": "https://storage.googleapis.com/kultura-image/workshop-4.jpg",
                "name": "Gamelan Music Workshop",
                "informasi": "Join our workshop to learn the traditional Balinese Gamelan music. Discover the unique instruments and rhythms of Gamelan.",
                "date": "2023-01-15",
                "time": "3:00 PM - 5:00 PM",
                "location": "Kultura Art Studio"
            }
        }
    ]
}