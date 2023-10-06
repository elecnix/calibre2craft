# calibre2color

Converts from Calibre JSON highlight to colored Markdown.

Calibre can export to Markdown, but does not preserve coloring. This script uses the JSON export to preserve colors by adding unicode color markers.

This python program converts the input JSON file (passed as argument) to a markdown file, appending `.md`. Highlights with the same chapter information will appear under the same Markdown header.

Markdown doesn't support color, so we add unicode characters:

    🔴 red
    🟠 orange
    ⚫ black
    ⚪ white
    🟣 purple
    🟢 green
    🟡 yellow
    🔵 blue


Simplified calibre JSON export example:

    {
        "highlights": [
            {
                "highlighted_text": "In fact, research by Google on their own teams found that who is on the team matters less than the team dynamics; and that when it comes to measuring performance, teams matter more than individuals.",
                "notes": "Look into this",
                "style": {
                    "kind": "color",
                    "type": "builtin",
                    "which": "yellow"
                },
                "toc_family_titles": [
                    "PART I TEAMS AS THE MEANS OF DELIVERY",
                    "Chapter 3: Team-First Thinking"
                ],
                "type": "highlight"
            }
        ],
        "type": "calibre_highlights",
        "version": 1
    }

Sample output:

    # Highlights
    ## PART I TEAMS AS THE MEANS OF DELIVERY
    ### Chapter 3: Team-First Thinking

    🟡 In fact, research by Google on their own teams found that who is on the team matters less than the team dynamics; and that when it comes to measuring performance, teams matter more than individuals.
    
    > Look into this

Multi-line highlights are represented as bullet items:

    🟡 For teams to work, team members should put the needs of the team above their own. They should:

    - Arrive for stand-ups and meetings on time.
    - Keep discussions and investigations on track.
    - Encourage a focus on team goals.
    - Help unblock other team members before starting on new work.
    - Mentor new or less experienced team members.
    - Avoid “winning” arguments and, instead, agree to explore options.
