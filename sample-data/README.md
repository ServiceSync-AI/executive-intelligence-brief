# Sample Test Data

This directory contains sample files for testing the ingestion pipeline.

## Files

- `test-agenda.pdf` - Sample meeting agenda (placeholder)
- `test-notes.docx` - Sample meeting notes (placeholder)
- `test-takeaways.jpg` - Sample handwritten takeaways (placeholder)

## Usage

Test ingestion with:

```bash
python ingest/ingest.py --file ./sample-data/test-agenda.pdf --dry-run
```

## Adding Real Data

Replace these placeholders with actual NADA meeting files when ready to process.

**Security Note:** Do not commit files containing PII or confidential information.
