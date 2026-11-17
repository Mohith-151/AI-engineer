import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# Theme Colors
BG_APP = "#F8FAFC"
BG_CARD = "#FFFFFF"
BORDER_COLOR = "#E2E8F0"
TEXT_PRIMARY = "#0F172A"
TEXT_SECONDARY = "#64748B"
ACCENT = "#2563EB"
ACCENT_HOVER = "#1D4ED8"
DANGER = "#EF4444"
INPUT_BG = "#FFFFFF"

class DailyLogApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Daily Log Generator")
        self.root.geometry("760x860")
        self.root.minsize(620, 650)
        self.root.configure(bg=BG_APP)

        # Save directly into the exact folder where this .py script is located
        self.target_dir = os.path.dirname(os.path.abspath(__file__))

        self._build_ui()

    def _build_ui(self):
        # --- Top Header ---
        header = tk.Frame(self.root, bg=BG_CARD, highlightbackground=BORDER_COLOR, highlightthickness=1)
        header.pack(fill="x", side="top")

        header_inner = tk.Frame(header, bg=BG_CARD, padx=24, pady=14)
        header_inner.pack(fill="x")

        title_row = tk.Frame(header_inner, bg=BG_CARD)
        title_row.pack(fill="x")

        tk.Label(
            title_row,
            text="Daily Log Generator",
            font=("Segoe UI", 16, "bold"),
            fg=TEXT_PRIMARY,
            bg=BG_CARD,
        ).pack(side="left")

        self.filename_badge = tk.Label(
            title_row,
            text="→ Day-XX.md",
            font=("Consolas", 10, "bold"),
            fg=ACCENT,
            bg="#EFF6FF",
            padx=10,
            pady=4,
        )
        self.filename_badge.pack(side="right")

        tk.Label(
            header_inner,
            text=f"Saves directly to folder: {self.target_dir}",
            font=("Segoe UI", 9),
            fg=TEXT_SECONDARY,
            bg=BG_CARD,
            anchor="w",
        ).pack(fill="x", pady=(4, 0))

        # --- Scrollable Main Area ---
        container = tk.Frame(self.root, bg=BG_APP)
        container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(container, bg=BG_APP, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=BG_APP)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.bind('<Configure>', lambda event: self.canvas.itemconfig(self.canvas_window, width=event.width))
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Mousewheel scrolling support
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # --- Form Content ---
        content_pad = tk.Frame(self.scrollable_frame, bg=BG_APP, padx=24, pady=20)
        content_pad.pack(fill="both", expand=True)

        # Metadata Section
        meta_card = self._create_card(content_pad, "General Information")
        
        tk.Label(meta_card, text="Day Number / Title", font=("Segoe UI", 10, "bold"), fg=TEXT_PRIMARY, bg=BG_CARD).pack(anchor="w", pady=(0, 4))
        
        day_row = tk.Frame(meta_card, bg=BG_CARD)
        day_row.pack(fill="x", pady=(0, 12))
        
        self.day_entry = tk.Entry(day_row, font=("Segoe UI", 11), bg=INPUT_BG, relief="solid", bd=1)
        self.day_entry.pack(side="left", fill="x", expand=True, ipady=4)
        self.day_entry.insert(0, "Day 1: Getting Started")
        self.day_entry.bind("<KeyRelease>", self._update_filename_badge)

        tk.Label(meta_card, text="Date (DD-MM-YYYY)", font=("Segoe UI", 10, "bold"), fg=TEXT_PRIMARY, bg=BG_CARD).pack(anchor="w", pady=(0, 4))
        self.date_entry = tk.Entry(meta_card, font=("Segoe UI", 11), bg=INPUT_BG, relief="solid", bd=1)
        self.date_entry.pack(fill="x", ipady=4)
        self.date_entry.insert(0, datetime.now().strftime("%d-%m-%Y"))

        # 1. What I learned
        self.learned_frame, self.learned_entries = self._create_dynamic_list_section(
            content_pad, "What I learned (3-5 bullets)", initial_count=3
        )

        # 2. What I built or coded today
        self.built_frame, self.built_entries = self._create_dynamic_list_section(
            content_pad, "What I built or coded today", initial_count=1
        )

        # 3. What broke, and how I fixed it
        break_card = self._create_card(content_pad, "What broke, and how I fixed it")
        
        tk.Label(break_card, text="Problem", font=("Segoe UI", 10, "bold"), fg=TEXT_SECONDARY, bg=BG_CARD).pack(anchor="w", pady=(0, 2))
        self.prob_entry = tk.Entry(break_card, font=("Segoe UI", 10), bg=INPUT_BG, relief="solid", bd=1)
        self.prob_entry.pack(fill="x", ipady=3, pady=(0, 8))

        tk.Label(break_card, text="Cause", font=("Segoe UI", 10, "bold"), fg=TEXT_SECONDARY, bg=BG_CARD).pack(anchor="w", pady=(0, 2))
        self.cause_entry = tk.Entry(break_card, font=("Segoe UI", 10), bg=INPUT_BG, relief="solid", bd=1)
        self.cause_entry.pack(fill="x", ipady=3, pady=(0, 8))

        tk.Label(break_card, text="Fix", font=("Segoe UI", 10, "bold"), fg=TEXT_SECONDARY, bg=BG_CARD).pack(anchor="w", pady=(0, 2))
        self.fix_entry = tk.Entry(break_card, font=("Segoe UI", 10), bg=INPUT_BG, relief="solid", bd=1)
        self.fix_entry.pack(fill="x", ipady=3)

        # 4. One thing I still don't understand
        self.dont_frame, self.dont_entries = self._create_dynamic_list_section(
            content_pad, "One thing I still don't understand", initial_count=1
        )

        # 5. Self-test
        self.selftest_card = self._create_card(content_pad, "Self-test (answer without looking at notes)")
        self.selftest_items_frame = tk.Frame(self.selftest_card, bg=BG_CARD)
        self.selftest_items_frame.pack(fill="x")
        self.selftest_rows = []
        
        btn_st_frame = tk.Frame(self.selftest_card, bg=BG_CARD)
        btn_st_frame.pack(fill="x", pady=(8, 0))
        tk.Button(
            btn_st_frame, text="+ Add Question", font=("Segoe UI", 9, "bold"),
            bg="#F1F5F9", fg=ACCENT, relief="flat", padx=12, pady=6,
            cursor="hand2", command=lambda: self._add_selftest_row()
        ).pack(anchor="w")

        self._add_selftest_row()
        self._add_selftest_row()

        # 6. Tomorrow's first task
        self.tomorrow_frame, self.tomorrow_entries = self._create_dynamic_list_section(
            content_pad, "Tomorrow's first task", initial_count=1
        )

        # --- Bottom Action Bar ---
        footer_bar = tk.Frame(self.root, bg=BG_CARD, highlightbackground=BORDER_COLOR, highlightthickness=1)
        footer_bar.pack(fill="x", side="bottom")

        footer_inner = tk.Frame(footer_bar, bg=BG_CARD, padx=24, pady=14)
        footer_inner.pack(fill="x")

        tk.Button(
            footer_inner, text="Reset Form", font=("Segoe UI", 10),
            bg="#F1F5F9", fg=TEXT_SECONDARY, relief="flat", padx=16, pady=8,
            cursor="hand2", command=self._reset_form
        ).pack(side="left")

        tk.Button(
            footer_inner, text="Generate & Save .md File", font=("Segoe UI", 11, "bold"),
            bg=ACCENT, fg="#FFFFFF", activebackground=ACCENT_HOVER, activeforeground="#FFFFFF",
            relief="flat", padx=20, pady=8, cursor="hand2", command=self._generate_markdown
        ).pack(side="right")

        self._update_filename_badge()

    def _create_card(self, parent, title):
        card = tk.Frame(parent, bg=BG_CARD, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=16, pady=16)
        card.pack(fill="x", pady=(0, 16))
        
        tk.Label(
            card, text=title, font=("Segoe UI", 11, "bold"),
            fg=TEXT_PRIMARY, bg=BG_CARD
        ).pack(anchor="w", pady=(0, 10))
        return card

    def _create_dynamic_list_section(self, parent, title, initial_count=1):
        card = self._create_card(parent, title)
        items_frame = tk.Frame(card, bg=BG_CARD)
        items_frame.pack(fill="x")

        entries = []

        def add_row(default_val=""):
            row = tk.Frame(items_frame, bg=BG_CARD)
            row.pack(fill="x", pady=(0, 6))

            ent = tk.Entry(row, font=("Segoe UI", 10), bg=INPUT_BG, relief="solid", bd=1)
            ent.pack(side="left", fill="x", expand=True, ipady=3)
            if default_val:
                ent.insert(0, default_val)

            if len(entries) > 0:
                del_btn = tk.Button(
                    row, text="×", font=("Segoe UI", 11, "bold"),
                    fg=DANGER, bg=BG_CARD, relief="flat", padx=6,
                    cursor="hand2", command=lambda r=row, e=ent: self._remove_row(r, e, entries)
                )
                del_btn.pack(side="right", padx=(6, 0))

            entries.append(ent)

        btn_frame = tk.Frame(card, bg=BG_CARD)
        btn_frame.pack(fill="x", pady=(6, 0))

        tk.Button(
            btn_frame, text="+ Add Bullet Point", font=("Segoe UI", 9, "bold"),
            bg="#F1F5F9", fg=ACCENT, relief="flat", padx=12, pady=6,
            cursor="hand2", command=lambda: add_row()
        ).pack(anchor="w")

        for _ in range(initial_count):
            add_row()

        return items_frame, entries

    def _remove_row(self, row_frame, entry_widget, entry_list):
        if entry_widget in entry_list:
            entry_list.remove(entry_widget)
        row_frame.destroy()

    def _add_selftest_row(self):
        row_card = tk.Frame(self.selftest_items_frame, bg="#F8FAFC", highlightbackground=BORDER_COLOR, highlightthickness=1, padx=10, pady=10)
        row_card.pack(fill="x", pady=(0, 8))

        top_r = tk.Frame(row_card, bg="#F8FAFC")
        top_r.pack(fill="x")

        lbl_num = tk.Label(top_r, text=f"Question {len(self.selftest_rows)+1}", font=("Segoe UI", 9, "bold"), fg=TEXT_SECONDARY, bg="#F8FAFC")
        lbl_num.pack(side="left")
        
        if len(self.selftest_rows) > 0:
            tk.Button(
                top_r, text="Remove", font=("Segoe UI", 8, "bold"),
                fg=DANGER, bg="#F8FAFC", relief="flat", cursor="hand2",
                command=lambda rc=row_card: self._remove_selftest_row(rc)
            ).pack(side="right")

        q_entry = tk.Entry(row_card, font=("Segoe UI", 10), bg=INPUT_BG, relief="solid", bd=1)
        q_entry.pack(fill="x", ipady=2, pady=(4, 6))

        tk.Label(row_card, text="Answer", font=("Segoe UI", 9, "bold"), fg=TEXT_SECONDARY, bg="#F8FAFC").pack(anchor="w", pady=(0, 2))
        a_entry = tk.Entry(row_card, font=("Segoe UI", 10), bg=INPUT_BG, relief="solid", bd=1)
        a_entry.pack(fill="x", ipady=2)

        self.selftest_rows.append((q_entry, a_entry, row_card))

    def _remove_selftest_row(self, row_card):
        for item in list(self.selftest_rows):
            if item[2] == row_card:
                self.selftest_rows.remove(item)
                break
        row_card.destroy()

    def _update_filename_badge(self, event=None):
        day_text = self.day_entry.get().strip()
        match = re.search(r'day\s*-?(\d+)', day_text, re.IGNORECASE)
        if match:
            slug = f"Day-{match.group(1)}.md"
        else:
            clean_name = re.sub(r'[^a-zA-Z0-9]+', '-', day_text).strip('-')
            slug = f"{clean_name}.md" if clean_name else "Day-XX.md"
        self.filename_badge.config(text=f"→ {slug}")

    def _reset_form(self):
        if messagebox.askyesno("Reset Form", "Are you sure you want to clear all fields?"):
            self.day_entry.delete(0, tk.END)
            self.day_entry.insert(0, "Day 1: Topic")
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, datetime.now().strftime("%d-%m-%Y"))
            self.prob_entry.delete(0, tk.END)
            self.cause_entry.delete(0, tk.END)
            self.fix_entry.delete(0, tk.END)
            self._update_filename_badge()

    def _generate_markdown(self):
        day_val = self.day_entry.get().strip()
        date_val = self.date_entry.get().strip()

        if not day_val:
            messagebox.showerror("Error", "Please enter the day title (e.g. Day 1: Python Basics)")
            return

        if not day_val.lower().startswith("#"):
            day_header = f"# {day_val}"
        else:
            day_header = day_val

        learned = [e.get().strip() for e in self.learned_entries if e.get().strip()]
        built = [e.get().strip() for e in self.built_entries if e.get().strip()]
        dont = [e.get().strip() for e in self.dont_entries if e.get().strip()]
        tomorrow = [e.get().strip() for e in self.tomorrow_entries if e.get().strip()]

        md_lines = [
            "# Daily Log Template",
            "---",
            "",
            f"{day_header}",
            "",
            f"**Date:** {date_val}",
            "",
            "---",
            "",
            "## What I learned (3-5 bullets)"
        ]
        
        if learned:
            for item in learned:
                md_lines.append(f"- {item}")
        else:
            md_lines.append("- ")

        md_lines.extend([
            "",
            "## What I built or coded today",
            "(link to the notebook or file in this repo)"
        ])
        if built:
            for item in built:
                md_lines.append(f"- {item}")
        else:
            md_lines.append("- ")

        md_lines.extend([
            "",
            "## What broke, and how I fixed it",
            f"- Problem: {self.prob_entry.get().strip()}",
            f"- Cause: {self.cause_entry.get().strip()}",
            f"- Fix: {self.fix_entry.get().strip()}",
            "",
            "## One thing I still don't understand"
        ])
        if dont:
            for item in dont:
                md_lines.append(f"- {item}")
        else:
            md_lines.append("- ")

        md_lines.extend([
            "",
            "## Self-test (answer without looking at notes)"
        ])
        
        if self.selftest_rows:
            for idx, (q, a, _) in enumerate(self.selftest_rows, 1):
                md_lines.append(f"{idx}. Q: {q.get().strip()}")
                md_lines.append(f"   A: {a.get().strip()}")
        else:
            md_lines.append("1. Q: \n   A: ")

        md_lines.extend([
            "",
            "## Tomorrow's first task"
        ])
        if tomorrow:
            for item in tomorrow:
                md_lines.append(f"- {item}")
        else:
            md_lines.append("- ")

        md_lines.extend([
            "",
            "---",
            "---"
        ])

        content = "\n".join(md_lines)

        match = re.search(r'day\s*-?(\d+)', day_val, re.IGNORECASE)
        if match:
            filename = f"Day-{match.group(1)}.md"
        else:
            clean_name = re.sub(r'[^a-zA-Z0-9]+', '-', day_val).strip('-')
            filename = f"{clean_name}.md" if clean_name else "Daily-Log.md"

        filepath = os.path.join(self.target_dir, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Success!", f"Successfully generated and saved:\n{filename}\n\nFolder:\n{self.target_dir}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyLogApp(root)
    root.mainloop()