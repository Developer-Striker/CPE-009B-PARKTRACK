class Styles:
    # Color Palette Constants
    BACKGROUND_COLOR = "#2d2d30"
    SIDEBAR_COLOR = "#3e3e42"
    BORDER_COLOR = "#555"
    BORDER_DARK = "#444"
    TERMINAL_COLOR = "#1e1e1e"
    ROAD_COLOR = "#282828"
    ROAD_DASH_COLOR = "#777"
    
    ACCENT_GOLD = "#f1c40f"
    ACCENT_RED = "#e74c3c"
    ACCENT_GREEN = "#2ecc71"
    ACCENT_BLUE = "#2980b9"
    ACCENT_GRAY = "#7f8c8d"
    
    TEXT_MUTED = "color: #aaa;"
    TEXT_LIGHT_GRAY = "color: #ccc;"

    @staticmethod
    def apply_widget_styles(app_window):
        """Applies explicit Python-level style overrides that QSS doesn't handle natively."""
        # Main Window background
        app_window.setStyleSheet(f"background-color: {Styles.BACKGROUND_COLOR};")

        # Container Frames
        app_window.right_sidebar_container.setStyleSheet(
            f"background-color: {Styles.SIDEBAR_COLOR}; border-radius: 6px; border: 2px solid {Styles.BORDER_COLOR};"
        )
        
        # Section Header Labels (Prevents default QSS box outline artifacts)
        app_window.lbl_checkin_section.setStyleSheet(f"color: {Styles.ACCENT_GOLD}; font-size: 13px; font-weight: bold; border: none;")
        app_window.lbl_billing_section.setStyleSheet(f"color: {Styles.ACCENT_RED}; font-size: 13px; font-weight: bold; border: none;")
        app_window.log_title.setStyleSheet("color: white; font-size: 12px; font-weight: bold; border: none; padding-top: 5px;")
        
        # Subtext Labels
        for lbl in app_window.subtext_labels:
            lbl.setStyleSheet(f"{Styles.TEXT_MUTED} border: 1px solid #555;")
            
        for lbl in app_window.rate_subtext_labels:
            lbl.setStyleSheet(f"{Styles.TEXT_LIGHT_GRAY} border: 1px solid #555;")

        # Custom Styled Input Fields
        app_window.customer_name_input.setStyleSheet(
            f"background-color: {Styles.BORDER_COLOR}; color: white; border: 1px solid {Styles.ROAD_DASH_COLOR}; padding: 5px; border-radius: 3px;"
        )
        app_window.spot_selector.setStyleSheet(
            f"background-color: {Styles.BORDER_COLOR}; color: white; border: 1px solid {Styles.ROAD_DASH_COLOR}; padding: 5px; border-radius: 3px;"
        )
        app_window.active_spot_selector.setStyleSheet(
            f"background-color: {Styles.BORDER_COLOR}; color: white; padding: 5px; border-radius: 3px;"
        )
        
        # SpinBoxes
        app_window.base_rate_spin.setStyleSheet(f"background-color: {Styles.BORDER_COLOR}; color: white; padding: 3px;")
        app_window.hourly_rate_spin.setStyleSheet(f"background-color: {Styles.BORDER_COLOR}; color: white; padding: 3px;")
        
        # Rate Frame Box
        app_window.rate_box.setStyleSheet(f"background-color: {Styles.BACKGROUND_COLOR}; border: 1px solid {Styles.BORDER_COLOR}; border-radius: 4px;")
        
        # Action Buttons
        app_window.btn_assign.setStyleSheet(
            f"background-color: {Styles.ACCENT_BLUE}; color: white; font-weight: bold; padding: 8px; border-radius: 4px; margin-top: 5px;"
        )
        app_window.btn_checkout.setStyleSheet(
            f"background-color: {Styles.ACCENT_RED}; color: white; font-weight: bold; padding: 8px; border-radius: 4px; margin-top: 5px;"
        )

        # Activity Log Box
        app_window.activity_log_box.setStyleSheet(
            f"background-color: {Styles.TERMINAL_COLOR}; color: {Styles.ACCENT_GREEN}; border: 1px solid {Styles.BORDER_COLOR}; font-family: Courier; font-size: 11px; border-radius: 4px;"
        )

        # Banner & Stat Box Elements
        app_window.banner.setStyleSheet(f"background-color: {Styles.SIDEBAR_COLOR}; border-radius: 6px; border: 1px solid {Styles.BORDER_COLOR};")
        app_window.p_logo.setStyleSheet(f"background-color: {Styles.TERMINAL_COLOR}; color: {Styles.ACCENT_GOLD}; font-size: 20px; font-weight: bold; border-radius: 4px;")
        app_window.hub_title.setStyleSheet("color: white; font-size: 18px; font-weight: bold; background: transparent; border: none;")
        
        # Map Scroll Area & Grid
        app_window.scroll_area.setStyleSheet(f"QScrollArea {{ border: 1px solid {Styles.BORDER_COLOR}; border-radius: 6px; background-color: {Styles.TERMINAL_COLOR}; }}")
        app_window.grid_frame.setStyleSheet(f"background-color: {Styles.TERMINAL_COLOR};")
        
        # Filter Strip
        app_window.lbl_filter.setStyleSheet(f"{Styles.TEXT_MUTED} font-size: 12px; font-weight: bold; border: none;")
        app_window.btn_all.setStyleSheet(f"background-color: {Styles.ACCENT_GRAY}; color: white; font-weight: bold; padding: 4px 12px; border-radius: 3px;")
        app_window.btn_avail.setStyleSheet(f"background-color: {Styles.ACCENT_GREEN}; color: white; font-weight: bold; padding: 4px 12px; border-radius: 3px;")
        app_window.btn_occ.setStyleSheet(f"background-color: {Styles.ACCENT_RED}; color: white; font-weight: bold; padding: 4px 12px; border-radius: 3px;")
