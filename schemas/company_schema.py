schema = {
    "type": "object",
    "properties": {
        "company_id": {
            "type": "integer"
        },
        "company_name": {
            "type": "string"
        },
        "company_address": {
            "type": "string"
        },
        "company_status": {
            "type": "string"
        },
        "description_lang": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "translation_lang": {
                        "type": "string"
                    },
                    "translation": {
                        "type": "string"
                    }
                },
                "required": [
                    "translation_lang",
                    "translation"
                ]
            }
        }
    },
    "required": [
        "company_id",
        "company_name",
        "company_address",
        "company_status",
        "description_lang"
    ]
}
