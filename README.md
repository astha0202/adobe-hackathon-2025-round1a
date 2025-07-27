# 📘 Round 1A – PDF Title and Heading Extractor

A Python-based tool that processes PDF documents to extract:

- The most likely document title
- Hierarchical headings (H1, H2, H3) based on font size and layout
- Outputs the result as structured JSON per file

The solution runs efficiently in a Docker container without requiring internet access.

---

## 📌 Approach

The extractor uses the following strategies to identify document structure:

1. **Title Extraction**:
   - Primary: Extracts from PDF metadata (if available)
   - Fallback: Detects prominent text on the first page

2. **Heading Detection**:
   - Analyzes font characteristics (size, weight)
   - Uses adaptive size thresholds:
     - ≥ 20 pt → H1
     - 16–19.99 pt → H2
     - 12–15.99 pt → H3
   - Skips noisy lines or overly long spans (e.g., >30 words)

3. **Performance Optimization**:
   - Memory-efficient: processes one page at a time
   - Early discards of non-heading content
   - Runs completely offline
   - Fast execution (<10s per document)

---

## 📂 Project Structure

