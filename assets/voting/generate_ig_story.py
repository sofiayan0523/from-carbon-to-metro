#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Set up paths
ROOT = Path("/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674")
MASCOT_PATH = ROOT / "from-carbon-to-metro" / "assets/voting/vote-submit-v2-A-mascot-768x514.png"
OUTPUT_PNG = ROOT / "from-carbon-to-metro" / "assets/voting/vote-submit-ig-story-1080x1920.png"
OUTPUT_WEBP = ROOT / "from-carbon-to-metro" / "assets/voting/vote-submit-ig-story-1080x1920.webp"

# Fonts
FONT_BLACK = ROOT / ".omni/tmp/fonts/NotoSansCJKtc-Black.otf"
FONT_BOLD = ROOT / ".omni/tmp/fonts/NotoSansCJKtc-Bold.otf"
FONT_REG = ROOT / "from-carbon-to-metro" / "assets/fonts/NotoSansCJKtc-Regular.otf"

# Colors
COLOR_BG = (243, 225, 43)       # Highly energetic vibrant yellow #F3E12B
COLOR_DARK = (26, 26, 26)       # Neo-brutalism black #1A1A1A
COLOR_WHITE = (255, 255, 255)   # Pure white #FFFFFF
COLOR_RED = (237, 93, 41)       # Coral Red #ED5D29 (Numbers brand red)
COLOR_PINK = (249, 198, 192)    # Soft pink #F9C6C0 (Numbers brand pink)
COLOR_GREEN = (127, 156, 126)   # Soft green #7F9C7E (Numbers brand green)

def get_font(path, size):
    try:
        return ImageFont.truetype(str(path), size)
    except Exception as e:
        print(f"Error loading font {path}, falling back to default. Error: {e}")
        return ImageFont.load_default()

def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]

def draw_centered_text(draw, text, font, y, color):
    w = text_width(draw, text, font)
    x = (1080 - w) // 2
    draw.text((x, y), text, font=font, fill=color)

def main():
    if not MASCOT_PATH.exists():
        print(f"Mascot image not found at {MASCOT_PATH}!")
        sys.exit(1)

    print(f"Creating 1080x1920 IG Story Canvas...")
    # Create canvas
    canvas = Image.new("RGB", (1080, 1920), COLOR_BG)
    draw = ImageDraw.Draw(canvas)

    # 1. Subtle dotted background pattern or grid for a trendy tech vibe
    dot_spacing = 60
    dot_radius = 2
    for x in range(dot_spacing, 1080, dot_spacing):
        for y in range(dot_spacing, 1920, dot_spacing):
            draw.ellipse(
                [(x - dot_radius, y - dot_radius), (x + dot_radius, y + dot_radius)],
                fill=(210, 195, 30)  # slightly darker yellow for subtle effect
            )

    # 2. Outer stylish border (Neo-brutalism inner frame)
    draw.rectangle([(24, 24), (1056, 1896)], outline=COLOR_DARK, width=6)

    # 3. Top Header Section
    f_kicker = get_font(FONT_BOLD, 36)
    f_main_title = get_font(FONT_BLACK, 52)

    # Draw Kicker
    draw_centered_text(draw, "2026 臺北捷運黑客松決賽", f_kicker, 110, COLOR_DARK)

    # Draw main title badge (Neo-brutalism capsule)
    badge_x1, badge_y1 = 120, 175
    badge_x2, badge_y2 = 960, 285
    # Shadow
    draw.rectangle([(badge_x1 + 10, badge_y1 + 10), (badge_x2 + 10, badge_y2 + 10)], fill=COLOR_DARK)
    # Card
    draw.rectangle([(badge_x1, badge_y1), (badge_x2, badge_y2)], fill=COLOR_WHITE, outline=COLOR_DARK, width=6)
    # Text inside card
    title_text = "★ 人氣票選 ‧ 誠摯邀票 ★"
    tw = text_width(draw, title_text, f_main_title)
    tx = badge_x1 + (badge_x2 - badge_x1 - tw) // 2
    ty = badge_y1 + (badge_y2 - badge_y1 - 60) // 2 - 2
    draw.text((tx, ty), title_text, font=f_main_title, fill=COLOR_DARK)

    # 4. Mascot Image Frame & Placement
    mascot_img = Image.open(MASCOT_PATH)
    # Resize keeping aspect ratio (width=930)
    target_w = 930
    aspect_ratio = mascot_img.size[0] / mascot_img.size[1]
    target_h = int(target_w / aspect_ratio) # ~622px
    mascot_resized = mascot_img.resize((target_w, target_h), Image.Resampling.LANCZOS)

    mx = (1080 - target_w) // 2 # 75
    my = 350

    # Draw Neo-brutalism shadow card for Mascot
    draw.rectangle([(mx + 12, my + 12), (mx + target_w + 12, my + target_h + 12)], fill=COLOR_DARK)
    # Draw Mascot Card outline
    draw.rectangle([(mx, my), (mx + target_w, my + target_h)], fill=COLOR_WHITE, outline=COLOR_DARK, width=6)
    # Paste resized mascot
    canvas.paste(mascot_resized, (mx + 3, my + 3)) # Slightly offset to keep inside the 6px border

    # 5. Accent badge on the Mascot Image (top right corner)
    # "入圍決賽 10 強"
    f_badge = get_font(FONT_BLACK, 30)
    badge_text = " 決賽 10 強入圍! "
    btw = text_width(draw, badge_text, f_badge)
    bx1, by1 = mx + target_w - btw - 40, my - 25
    bx2, by2 = mx + target_w - 20, my + 35
    # shadow
    draw.rectangle([(bx1 + 6, by1 + 6), (bx2 + 6, by2 + 6)], fill=COLOR_DARK)
    # body
    draw.rectangle([(bx1, by1), (bx2, by2)], fill=COLOR_RED, outline=COLOR_DARK, width=4)
    # text
    draw.text((bx1 + 10, by1 + 12), badge_text, font=f_badge, fill=COLOR_WHITE)

    # 6. Slogan / Project Info Below Mascot
    f_proj_title = get_font(FONT_BLACK, 84)
    f_sub_slogan = get_font(FONT_BOLD, 38)

    # Title shadow text for 3D effect
    title_text = "從碳客變捷客"
    # Draw shadow first
    w_t = text_width(draw, title_text, f_proj_title)
    tx = (1080 - w_t) // 2
    draw.text((tx + 6, 1020 + 6), title_text, font=f_proj_title, fill=COLOR_DARK)
    # Draw front text (Pinkish cream or pure white)
    draw.text((tx, 1020), title_text, font=f_proj_title, fill=COLOR_WHITE)
    # Draw border outline on the text
    for dx, dy in [(-2,-2), (2,-2), (-2,2), (2,2), (-2,0), (2,0), (0,-2), (0,2)]:
        draw.text((tx+dx, 1020+dy), title_text, font=f_proj_title, fill=COLOR_DARK)
    draw.text((tx, 1020), title_text, font=f_proj_title, fill=COLOR_WHITE)

    # Sub slogan
    draw_centered_text(draw, "搭捷運 ‧ 賺點數 ‧ 順手領好康！", f_sub_slogan, 1140, COLOR_DARK)

    # 7. Voting Steps Card
    step_x1, step_y1 = 75, 1220
    step_x2, step_y2 = 1005, 1690
    # Shadow
    draw.rectangle([(step_x1 + 14, step_y1 + 14), (step_x2 + 14, step_y2 + 14)], fill=COLOR_DARK)
    # Main card
    draw.rectangle([(step_x1, step_y1), (step_x2, step_y2)], fill=COLOR_WHITE, outline=COLOR_DARK, width=6)

    # Card Title Header (Black bar)
    draw.rectangle([(step_x1, step_y1), (step_x2, step_y1 + 80)], fill=COLOR_DARK)
    f_step_header = get_font(FONT_BOLD, 36)
    step_header_txt = "簡單 3 步驟 ‧ 投下關鍵一票！"
    stw = text_width(draw, step_header_txt, f_step_header)
    draw.text((step_x1 + (step_x2 - step_x1 - stw) // 2, step_y1 + 20), step_header_txt, font=f_step_header, fill=COLOR_WHITE)

    # Steps Text
    f_steps = get_font(FONT_BOLD, 34)
    f_steps_highlight = get_font(FONT_BLACK, 36)

    steps_data = [
        ("1. 手機下載並開啟 「台北捷運Go」 App", 1335, None),
        ("2. 點擊首頁 「捷運盃黑客松人氣票選」 Banner", 1410, None),
        ("3. 搜尋首字 ", 1485, "從碳客變捷客")
    ]

    for txt, y_pos, hl in steps_data:
        if hl:
            # Render "3. 搜尋首字" + highlighted "從碳客變捷客" + " 投下支持！"
            w_part1 = text_width(draw, txt, f_steps)
            w_hl = text_width(draw, hl, f_steps_highlight)
            w_part2 = text_width(draw, " 投下支持！", f_steps)
            total_step_w = w_part1 + w_hl + w_part2
            start_x = step_x1 + 60
            
            # Draw part 1
            draw.text((start_x, y_pos), txt, font=f_steps, fill=COLOR_DARK)
            
            # Draw highlight yellow capsule behind "從碳客變捷客"
            hx1, hy1 = start_x + w_part1 - 4, y_pos - 4
            hx2, hy2 = hx1 + w_hl + 8, y_pos + 46
            draw.rectangle([(hx1, hy1), (hx2, hy2)], fill=COLOR_BG, outline=COLOR_DARK, width=2)
            draw.text((hx1 + 4, y_pos - 2), hl, font=f_steps_highlight, fill=COLOR_DARK)
            
            # Draw part 2
            draw.text((hx2 + 4, y_pos), " 投下支持！", font=f_steps, fill=COLOR_DARK)
        else:
            draw.text((step_x1 + 60, y_pos), txt, font=f_steps, fill=COLOR_DARK)

    # Daily reminder at the bottom of the card
    f_reminder = get_font(FONT_BOLD, 32)
    reminder_txt = "★ 貼心提醒：每個會員帳號每天可投 1 票！"
    draw_centered_text(draw, reminder_txt, f_reminder, 1585, COLOR_RED)

    # 8. Footer Section
    f_url = get_font(FONT_BOLD, 30)
    f_footer_tech = get_font(FONT_REG, 24)

    # Showcase Link
    url_txt = "體驗互動 Demo ▶ from-carbon-metro-vote.pages.dev"
    draw_centered_text(draw, url_txt, f_url, 1735, COLOR_DARK)

    # Tech Support line
    tech_txt = "Omni Edge ｜ Numbers Protocol 共同提供技術支持"
    draw_centered_text(draw, tech_txt, f_footer_tech, 1805, COLOR_DARK)

    # Save outputs
    canvas.save(OUTPUT_PNG, "PNG")
    canvas.save(OUTPUT_WEBP, "WEBP", quality=85)
    print(f"Successfully generated IG Story images:")
    print(f" - PNG: {OUTPUT_PNG} ({OUTPUT_PNG.stat().st_size / 1024:.1f} KB)")
    print(f" - WEBP: {OUTPUT_WEBP} ({OUTPUT_WEBP.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    main()
