# Source licenses

Checked 2026-10-31.

| Source | Declared license | Decision |
|---|---|---|
| MathNet v0 (ShadenA/MathNet, MIT) | CC BY 4.0, with a carve-out: where a country or contest organization asserts its own copyright, that copyright is retained and takes precedence (card says permission to share was obtained from national team leaders). Per-row fields: `country`, `competition`, `booklet_source`. | **Use.** Exclude rows with an asserted copyright; attribute country/competition per problem; cite the paper (Alshammari et al., ICLR 2026). |
| MATH (Hendrycks) | MIT (reported; LICENSE text not read) | **Skip.** Problems originate with MAA via AoPS; authors' claim that MAA rights lapsed is unverified. |
| NuminaMath-1.5 | Apache-2.0 | **Skip.** Scraped from AoPS and exam sites; label covers only the compilers' work. |
| OTIS / Evan Chen handouts | None; excerpts book says "All rights reserved" | **Skip.** |
| AoPS wiki/forum, MAA | Copyrighted | **Skip.** Not scraped. |
| Ramp problems | Original, written for this project | Own work. |

## Notes
- The MathNet card says per-row fields `country`, `competition` and `booklet_source` identify rows where a national team asserts copyright. The parquet files we downloaded have no `booklet_source` column, so asserted-copyright rows cannot be filtered automatically. Every MathNet-derived problem keeps its country and contest, shown after the solution and on the Credits page. Before a public launch, contact the maintainer (shaden@mit.edu) to get the list of asserted-copyright contests and drop those.
- MathNet solutions were not used verbatim. Of the 24 pilot problems, several official solutions had gaps or errors (an unjustified step, a missing case, a wrong edge case); all solutions here were rewritten and independently checked.
