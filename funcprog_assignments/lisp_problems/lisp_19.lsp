;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun find-min-max (lst)
  (if (null lst)
      (cons nil nil)
      (let ((min-elem (car lst))
            (max-elem (car lst)))
        (dolist (num (cdr lst))
          (when (< num min-elem)
            (setq min-elem num))
          (when (> num max-elem)
            (setq max-elem num)))
        (cons min-elem max-elem))))
