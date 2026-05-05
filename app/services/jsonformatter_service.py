import json


class JsonFormatterService:
    @staticmethod
    def format_json(json_str: str, indentation: int):
        try:
            parsed = json.loads(json_str)
            formatted = json.dumps(parsed, indent=indentation)
        except json.JSONDecodeError as e:
            return f"""
            <div class="text-red-600 mt-4">
                Invalid JSON: {str(e)}
            </div>
            """

        return f"""
        <div class="mt-4 p-3 max-h-96 w-full max-w-xl border rounded-lg text-sm overflow-auto">
            <pre id="formatted-json" class="whitespace-pre">{formatted}</pre>
        </div>
        <button type="button" onclick="copyToClipboard(this, 'formatted-json')"
            class="cursor-pointer mt-4 px-4 py-2 bg-green-600 text-white rounded-lg hover:scale-105 transition duration-75">
            Copy
        </button>
        """
