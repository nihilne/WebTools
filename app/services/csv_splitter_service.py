import csv
import io
import zipfile


class CsvSplitterService:
    ALLOWED_EXTENSIONS = {"csv"}

    @staticmethod
    def allowed_file(filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in CsvSplitterService.ALLOWED_EXTENSIONS
        )

    @staticmethod
    def split_file_to_zip(file, chunk_size: int, has_header: bool):
        stream = io.TextIOWrapper(file.stream, encoding="utf-8", newline="")
        reader = csv.reader(stream)
        header = next(reader, None) if has_header else None
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            chunk = []
            file_index = 1

            for row in reader:
                chunk.append(row)

                if len(chunk) >= chunk_size:
                    CsvSplitterService._add_to_zip(zip_file, header, chunk, file_index)
                    file_index += 1
                    chunk = []

            # flush remainder
            if chunk:
                CsvSplitterService._add_to_zip(zip_file, header, chunk, file_index)

        zip_buffer.seek(0)
        return zip_buffer

    @staticmethod
    def _add_to_zip(zip_file, header, chunk, index):
        output = io.StringIO()
        writer = csv.writer(output)
        if header is not None:
            writer.writerow(header)
        writer.writerows(chunk)
        zip_file.writestr(f"part_{index}.csv", output.getvalue())
